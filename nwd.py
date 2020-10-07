a = int(input("a: "))
b = int(input("b: "))

def gcd(a: int, b: int):
    if a%b == 0:
        return b
    else:
        while b != 0:
            c = a%b
            a = b
            b = c
        return a

print(gcd(a, b))