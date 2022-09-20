from time import sleep
from random import randint
print ('Jogo da advinhação!')
sleep(1)
print ('Pensando em um numero...')
sleep(1.5)
b = randint (0,5)
a = int(input('Tente adivinhar....\nEscolha um numero de 0 a 5: '))
print ('Analisando sua resposta...')
sleep(2)
if a == b:
    print (f'Você acertou!! O numero escolhido foi o numero {b}')
else:
    print (f'Você errou!! O numero escolhido foi o numero {b}')

print ('fim')