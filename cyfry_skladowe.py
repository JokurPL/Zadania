k = 54321
tab_cyfr = []

while(k!=0):
    ostatnia_cyfra = k%10
    print(ostatnia_cyfra)
    k = (k - ostatnia_cyfra)/10
    tab_cyfr.append(int(ostatnia_cyfra))

tab_cyfr.sort()
print(tab_cyfr)


