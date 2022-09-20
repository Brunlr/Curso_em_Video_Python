a = 0 #recebe o valor
b = 0 #variavel de condição
c = list()
while True:
    a = int(input('Digite um valor: '))
    if a in c:
        print ('Não é possivel adicionar valores duplicados, tente novamente...')
    else:
        c.append(a)
    while True:
        b = str(input('Deseja continuar? (S/N): ')).upper()
        if b == 'S' or b == 'N':
            break
        else:
            print ('Erro! Digite novamente.')
    if b=='N':
        print ('Você escolheu sair do programa.')
        break
        c.sort()
print (f'Você digitou os valores {c}')