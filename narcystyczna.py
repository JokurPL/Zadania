
def potega(a, n):
    return a**n

k = 4078

def sprawdz(k):
    liczba_elementarna = k

    tab_cyfr = []
    suma = 0
    
    while(k!=0):
        ostatnia_cyfra = k%10
        k = (k - ostatnia_cyfra)/10
        tab_cyfr.append(ostatnia_cyfra)

    tab_cyfr.sort()
    n = len(tab_cyfr)

    for a in tab_cyfr:
        x = potega(a, n)
        suma += x

    if int(suma) == liczba_elementarna:
        return True
    else:
        return False

print(sprawdz(k))