a = 0
c = 0
b = int(input('Digite um numero para saber a soma dele com os demais\nPara pausar a soma digite 999: '))
while b!=999:
    c+=1
    a = a+b
    b = int(input('Digite um numero: '))
print ('O resultado da soma de todos os {} numeros é: {}'.format(c,a))
