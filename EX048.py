a = str(input('Calculo de numeros impares multiplos de 3 de 1 até 500\nPressione enter para começar: '))
b = 0
d= 0
for c in range(1,500):
    if c%3==0 and c%2==1:
        d+=1
        b+=c
print (f'Foram encontrados {d} numeros e o valor total é {b}')