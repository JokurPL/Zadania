import math

a = int(input("Podstawa: "))
b = int(input("Wykladnik: "))

def pot(a,b):
    wynik = int(math.pow(a,b))
    miejsce_ostatniej_cyfr = len(str(wynik))-1
    print(str(wynik)[miejsce_ostatniej_cyfr])

pot(a,b)