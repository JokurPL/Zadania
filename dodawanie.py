import sys

n = int(input("Liczba liczb do zsmuowania: "))
x = input("Liczby do zsumowania(oddzielone spacja): ")

l = int(n)

suma = 0

for num in x.split():
    if int(n) > 0:
        suma += int(num)
        n -= 1
    else:
        break

print(suma)
