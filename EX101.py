def somaidade(atual):
    ano=int()
    idade = 2022-atual
    return idade


def analise(a):
    if a>65 or a >= 16 and 18 > a:
        print (f'Com {a} anos, o voto é OPCIONAL!')
    elif a>=18:
        print (f'Com {a} anos, o voto é OBRIGATÓRIO!')
    else:
        print (f'Com {a} anos, NÃO VOTA!')


a = int(input('Digite o ano de nascimento: '))
a = somaidade(a)
analise(a)