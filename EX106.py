def main():
    print('\033[1:97:43m=-' * 30)
    print('SISTEMA DE AJUDA PYHELP')
    print('=-' * 30)
    print('\033[m')


from time import sleep

while True:
    main()
    a = str(input('Função ou biblioteca: ')).lower()
    if a=='fim':
        break
    print ('\033[1:97:44m=-'*30)
    print (f'Acessando o manual do comando "{a}"')
    sleep(1)
    print ('=-'*30)
    print ('\033[m')
    print ('\033[1:30:107m')
    print (help(a))
    sleep(1)
    print ('\033[m')