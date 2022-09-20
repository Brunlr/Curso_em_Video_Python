print ('_'*20)
from random import randint
from time import sleep
d = 0 #contador numero nos jogos
print ('JOGO MEGA SENA')
print ('_'*20)
e = list() #lista
f = 0 #randint
a = int(input('Quantos jogos você quer que eu sorteie? '))
a+=1
print (f'\033[1;92mSORTEANDO \033[1;91m{a-1}\033[m \033[1;92mJOGOS\033[m')
for c in range (1,a):
    print (f'Jogo {c}:', end='')
    e.clear()
    d = 0
    while True:
        f = randint(1,60)
        if f in e:
            f = randint(1,60)
        else:
            e.append(f)
            d+=1
        if d==6:
            break
            print(end='\n')
    print (e)
print('Fim')
