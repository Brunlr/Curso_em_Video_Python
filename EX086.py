a = list() #lista source
b = list () #lista primaria
c = 0 #receptor
d = 0 #contador 1
e = 0 #contador 2
while True:
    e = 0
    for f in range (0,3):
        c = int(input(f'Digite um valor para [{d}, {e}]: '))
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
print ('=-'*30)

