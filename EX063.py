b = int(input('Digite o numero de elementos da sequencia: '))
d = 0
c = 1
print (f'{d} > {c}', end=' ')
cont = 3
while cont<=b:
    e = c + d
    print (f' >  {e} ', end='')
    d = c
    c = e
    cont+=1
print ('fim')