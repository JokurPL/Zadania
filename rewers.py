n = input()
n = n.split()

tab = []

for l in n:
    tab.append(int(l))
tab.reverse()
output = ""
for l in tab:
    output += str(l) + " "

print(output)