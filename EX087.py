a = list() #lista source
b = list () #lista primaria
c = 0 #receptor
d = 0 #contador 1
e = 0 #contador 2
i = 0 #valores pares
j = 0 #soma da terceira coluna
k = 0 #maior da segunda linha
while True:
    e = 0
    for f in range (0,3):
        c = int(input(f'Digite um valor para [{d}, {e}]: '))
        if d==1 and c>k:
            k = c
        if e == 2:
            j+=c
        if c%2==0:
            i+=c
        b.append(c)
        e+=1
    a.append(b[:])
    b.clear()
    d+=1
    if d==3:
        break
print ('=-'*30)
for h in range (0,3):
    if h>0:
        print (end='\n')
    for g in a[h]:
        print (f'[ {g} ]', end =' ')
print (end='\n')
print ('=-'*30)
print (f'A soma de todos os valores pares digitados é igual a {i}')
print (f'A soma da terceira coluna é igual a {j}')
print (f'O maior numero da segunda linha é {k}')