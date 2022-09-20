from random import randint
a = randint(1,10) #numero do computador
b = 0 #numero do usuario
d = 0 #impar ou par
c = 0 #numero de vitorias consecutivas
while True:
    print ('-=-'*10)
    print ('PAR OU IMPAR')
    print ('-=-'*10)
    b = int(input('Escolha um numero: '))
    d = int(input('Escolha:\n[ 1 ] Impar\n[ 2 ] Par: '))
    if (a+b)%2 == 0 and d ==2 or (a+b)%2 ==1 and d==1:
        print (f'Você ganhou! Eu escolhi {a} e você {b}')
        c+=1
    elif (a+b)%2 == 1 and d ==2 or (a+b)%2 ==0 and d==1:
        print(f'Você Perdeu! Eu escolhi {a} e você {b}')
        break
    else:
        print ('Erro! Tente novamente.')
print (f'Você conseguiu {c} vitorias consecutivas')