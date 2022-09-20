a = 0 #Recebe o numero
b = 0 #Quantidade de numeros
c = 0 #Soma dos numeros
while True:
    a = int(input('Digite um numero (999 Para parar): '))
    if a == 999:
        break
    c+=a
    b+=1
print (f'Você digitou {b} numeros e a soma de todos é {c}.')
