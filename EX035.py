from time import sleep
r1 = int(input('Digite o primeiro lado de seu triangulo: '))
r2 = int(input('Digite o segundo lado de seu retangulo: '))
r3 = int(input('Digite o terceiro lado do seu retangulo: '))
a= 0
b= 0
if r1> r2 and r1>r3:
    b = r2+r3
    a= r1
if r2> r1 and r2>r3:
    a = r2
    b= r3+r1
if r3>r1 and r3>r2:
    a = r3
    b = r1+r2

print ('Calculando....')
sleep(2)
if a>b:
    print ('É possivel ser feito um triangulo com esses valores!')
else:
    print ('Não é possivel fazer um triangulo com esses valores!')