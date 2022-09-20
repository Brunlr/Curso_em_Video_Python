a = int(input('Digite um numero para saber se ele é um numero primo: '))
tot = 0
for c in range(1,a+1):
    if a%c==0:
        print('\033[33m', end=' ')
        tot+=1
    else:
        print ('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO numero {a} foi divisivel {tot} vezes')
if tot ==2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')