from time import sleep
a = int(input('Digite o primeiro termo da PA: '))
b = int(input('Digite a razão da PA: '))
d = 0
c = 1
e = 0
while c != 0:
    d = a
    c = int(input('Quantos termos você deseja: '))
    for e in range (0,c,1):
        print (a)
        a = a+b
        sleep(1)
print ('fim')