a = 0
b = 0
print ('Digite seis numeros e será feita a soma apenas dos numeros pares.')
for c in range(1,7):
    a = int(input('Digite um numero: '))
    if a%2==0:
        b+=a
print (f'A soma total dos numeros pares é {b}')