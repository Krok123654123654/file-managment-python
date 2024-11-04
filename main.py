import argparse

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


