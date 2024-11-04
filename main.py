import argparse
import csv
import random
import os


# Mappings for days and times
days_order = ['pn', 'wt', 'śr', 'cz', 'pt', 'sb', 'nd']
days_full = {
   'pn': 'poniedziałek',
   'wt': 'wtorek',
   'śr': 'środa',
   'cz': 'czwartek',
   'pt': 'piątek',
   'sb': 'sobota',
   'nd': 'niedziela'
}

times_full = {
   'r': 'rano',
   'w': 'wieczorem'
}

def zapis_do_csv(filepath):
   ## Tworzy plik `Dane.csv` składający się z dokładnie dwóch linii: 
   ##Model; Wynik; Czas; 
   ##A ; 17 ; 465s; Wartości w drugiej lini są dobierane losowo ##
   headers = ["Model", "Wynik", "Czas"]
   model = random.choice(["A", "B", "C"])
   wynik = random.randint(0, 1000)
   czas = f"{random.randint(0, 1000)}s"

   with open(filepath, mode='w', newline='') as Dane:
        writer = csv.writer(Dane, delimiter=';')
        writer.writerow(headers)
        writer.writerow([model, wynik, czas])
   print("Utworzono Plik Dane.csv")

def odczyt_z_csv(catalog):
   ## Sumuje wartości z kolumny `Czas` dla wszystkich plików CSV w katalogu,
   ##gdzie `Model` wynosi 'A'. ##
   sum = 0
   for elder, _, files in os.walk(catalog): ## Przechodząc po wszystkich plikach danego katalogu##
      for file in files:
         if file.endswith('.csv'):   ## Wybieramy tylko te które mają rozszerzenie csv##
            filepath = os.path.join(elder, file)
            with open(filepath, mode='r') as file:   ##Odczytujemy plik##
               reader = csv.DictReader(file, delimiter=';')
               for row in reader:
                   if row['Model'] == 'A':##Jesli Model to A, wtedy dodajemu czas (najpierw usuwamy jednostke i zmieniamy na int)##
                      time_val = int(row['Czas'].replace('s', ''))
                      sum += time_val
   print("Suma Czasu dla danego katalogu to:" + str(sum) + "s")

def get_time(i,times):
   if (i < len(times)):
      return times_full.get(times[i])
   return times_full.get("r")

def generate_or_read_paths(args):
   paths = []
   days_index = 0
   for months, days in zip(args.months, args.days) :
      days_index = 0
      index1,index2 = 0, 0
      if("-" in days):
         parts = days.split("-")

         if(len(parts) > 2):
            raise ValueError("Zła składnia dni")

         index1 = days_order.index(parts[0])
         index2 = days_order.index(parts[1]) + 1
      else :
         index1 = days_order.index(days)
         index2 = index1 + 1
      for i in list(days_full.keys())[index1 : index2]:
            if(args.read_or_write !="t"):
               paths.append(os.path.join(os.getcwd(),months,days_full[i],get_time(days_index, args.times)))
            else :
               paths.append(os.path.join(os.getcwd(),months,days_full[i],get_time(days_index, args.times),"Dane.csv"))
            days_index+=1
   print(paths)
   if(args.read_or_write != "t"):
      for path in paths:
         odczyt_z_csv(path)
   else:
      for path in paths:
         os.makedirs(path, exist_ok=True)
         zapis_do_csv(path)



def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("--months", type=str, nargs='+', help="wybor miesiecy")
   parser.add_argument("--days", type=str, nargs='+', help="wybor dni")
   parser.add_argument(
      "--times", type=str, default="r", nargs="+", required = False, help="Jaka pora dnia (r/w), domyślnie rano"
   )
   parser.add_argument(
      "--read_or_write", type=str, default="t", nargs="+", required = False, help="Tworzenie lub odczyt(t/o), domyślnie odczyt"
   )
   args = parser.parse_args()


   if(len(args.miesiace) != len(args.dni)):
      raise ValueError("Dla każdego miesiąca musi być podany dzień")
