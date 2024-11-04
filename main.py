import argparse
import csv
import random

def zapis_do_csv(filepath):
   """ Tworzy plik `Dane.csv` składający się z dokładnie dwóch linii: 
   Model; Wynik; Czas; 
   A ; 17 ; 465s; Wartości w drugiej lini są dobierane losowo """
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
   """ Sumuje wartości z kolumny `Czas` dla wszystkich plików CSV w katalogu,
   gdzie `Model` wynosi 'A'. """
   sum = 0
   for elder, _, files in os.walk(catalog): """ Przechodząc po wszystkich plikach danego katalogu"""
      for file in files:
         if file.endswith('.csv'):   """ Wybieramy tylko te które mają rozszerzenie csv"""
            filepath = os.path.join(elder, file)
            with open(filepath, mode='r') as file:   """Odczytujemy plik"""
               reader = csv.DictReader(file, delimiter=';')
               for row in reader:
                   if row['Model'] == 'A':"""Jesli Model to A, wtedy dodajemu czas (najpierw usuwamy jednostke i zmieniamy na int)"""
                      time_val = int(row['Czas'].replace('s', ''))
                      sum += time_val
   print("Suma Czasu dla danego katalogu to:" + str(sum) + "s")
   

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("--miesiace", type=str, nargs='+', help="wybor miesiecy")
   parser.add_argument("--dni", type=str, nargs='+', help="wybor dni")
   parser.add_argument(
      "--pora_dnia", type=str, default="r", nargs="+", required = False, help="Jaka pora dnia (r/w), domyślnie rano"
   )
   parser.add_argument(
      "--tworzenie_odczyt", type=str, default="t", nargs="+", required = False, help="Tworzenie lub odczyt(t/o), domyślnie odczyt"
   )



   args = parser.parse_args()

   if(len(args.miesiace) != len(args.dni)):
      raise ValueError("Dla każdego miesiąca musi być podany dzień")


