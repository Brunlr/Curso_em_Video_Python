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


def leiafloat(txt):
    while True:
        try:
            a = float(input(txt))
        except KeyboardInterrupt:
            print()
            print('\033[1;31mO usuario optou por sair do programa!\033[m')
            a = 0
            return a
            break
        except:
            print('\033[1;31mErro! Por favor, digite um numero real válido\033[m')
        else:
            return a
            break


try:
    a = leiaint('Digite um número inteiro: ')
    b = leiafloat('Digite um número real: ')
finally:
    print(f'O valor inteiro digitado foi {a} e o real foi {b}')

