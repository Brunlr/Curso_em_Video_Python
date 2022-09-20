from random import randint
from time import sleep
b = str(input('Pressione enter para os numeros serem gerados:'))
a = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)) #tupla
d = 0 #maior
e = 0 #menor
print ('Os numeros escolhidos são:')
for c in a:
    if e==0:
        e=c
    elif e>c:
        e = c
    if c>d:
        d = c
    print (c)
    sleep(0.1)
print (f'O maior numero escolhido foi o {d}\nO menor numero escolhido foi o {e}')
