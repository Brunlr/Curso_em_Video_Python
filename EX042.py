from time import sleep
r1 = int(input('Digite o 1° lado do triangulo: '))
r2 = int(input('Digite o 2° lado do triangulo: '))
r3 = int(input('Digite o 3° lado do triangulo: '))


print ('Calculando....')
sleep(2)
if r1 + r2 > r3 or r1 + r3>r2 or r3+r1>r1:
    if r1==r2 and r2==r3:
        print ('Você formou um triangulo equilátero com todos os lados iguais')
    elif r1==r2 and r1 !=r3 or r3==r2 and r3!=r1 or r2==r1 and r2!= r3:
        print ('Você tem um triangulo isoceles com apenas dois lados iguais')
    elif r1!=r2 and r2!=r3 and r1!=r3:
        print ('Você tem um triangulo escaleno com todos os lados diferentes')
else:
    print ('Não é possivel fazer um triangulo com esses valores!')
print ('fim')