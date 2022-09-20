from random import randint
a = randint(0,10) #numero da maquina
b = int(input('Digite um numero de 0 a 10:'))
c = 1 #jogadas

while b!=a:
    c+=1
    print('RESPOSTA ERRADA!')
    b = int(input('Escolha novamente: '))
print (f'Você acertou, foi necessario apenas {c} palpite(s) para acertar')
