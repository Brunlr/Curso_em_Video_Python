a = int(input('Digite um numero de 0 a 9999: '))
print (f'Unidade {a//1%10}')
print (f'Dezena {a//10%10}')
print (f'Centena {a//100%10}')
print (f'Milhar {a//1000%10}')