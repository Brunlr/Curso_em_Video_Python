a= 0
b = list()  #lista par
d = list()  #lista impar
c = list()  #lista source
g = list() #lista crescente
for e in range (0,7):
    a = int(input('Digite um valor: '))
    g.append(a)
    if a % 2 == 0:
        b.append(a)

    else:
        d.append(a)
c.append(d)
c.append(b)
g.sort()
print (c)
print (g)
