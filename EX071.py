print ('-'*15)
print ('SIMULADOR DE CAIXA ELETRONICO')
print ('-'*15)
a = int(input('Digite o valor que você deseja sacar: '))#valor que vai diminuindo constatemente
b = 0 #notas
if a-50>=0:
    while True:
        a =a-50
        b = b+1
        if 50>a:
            break
print (f'São {b} notas de R$50,00')
if a-20>=0:
    b=0
    while True:
        a =a-20
        b = b+1
        if 20>a:
            break
print (f'São {b} notas de R$20,00')
if a-10>=0:
    b=0
    while True:
        a =a-10
        b = b+1
        if 10>a:
            break
print (f'São {b} notas de R$10,00')
if a-1>=0:
    b=0
    while True:
        a =a-1
        b = b+1
        if 1>a:
            break
print (f'São {b} notas de R$1,00')

print ('Fim')