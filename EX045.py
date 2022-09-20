from time import sleep
from random import randint
print ('JOKENPO')
b = randint(1,3)
if b==1:
    c = 'Pedra'
elif b==2:
    c = 'Papel'
elif b== 3:
    c = 'Tesoura'
a = int(input('Faça a escolha com seu respectivo numero:\n1- Pedra\n2-Papel\n3- Tesoura: '))
if a==1:
    d = 'Pedra'
elif a==2:
    d = 'Papel'
elif a== 3:
    d = 'Tesoura'
if a == b:
    print ('Empate!')
if a==1 and b==2 or a== 2 and b==3 or a==3 and b==1:
    print (f'Você Perdeu! Você escolheu {d} e eu escolhi {c}')
elif a==2 and b==1 or a== 3 and b==2 or a==1 and b==3:
    print (f'Você Ganhou! Você escolheu {d} e eu escolhi {c}')