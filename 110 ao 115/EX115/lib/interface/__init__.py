def leiaint(txt):
    while True:
        try:
            a = int(input(txt))
        except KeyboardInterrupt:
            print()
            print('\033[1;31mO usuario optou por sair do programa!\033[m')
            a=0
            return a
            break
        except:
            print('\033[1;31mErro! Por favor, digite um numero inteiro válido\033[m')
        else:
            return a
            break


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print (linha())
    print(txt.center(42))
    print (linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print (f'\033[32m{c}\033[m - \033[35m{item}\033[m')
        c+=1
    print (linha())
    opc = leiaint('\033[36mSua Opção: \033[m')
    return opc