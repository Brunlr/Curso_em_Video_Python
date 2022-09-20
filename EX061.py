from time import sleep
a = int(input('Digite o primeiro termo da PA: '))
b = int(input('Digite a razão da PA: '))
c = 0
while c!=10:
    c+=1
    print (a)
    a = a+b
    sleep(1)
print ('fim')