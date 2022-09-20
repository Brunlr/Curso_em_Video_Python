a = 0 #recebedor #
b = list() #lista
c = 0 #numeros digitados
d = 0 #condicional
while True:
    a  = int(input('Digite um numero: '))
    b.append(a)
    c+=1
    while True:
        d = str(input('Deseja continuar? (S/N): ')).upper()
        if 'S' or 'N' in d:
            break
        else:
            print ('Erro! Tente novamente')
    if 'N' in d:
        print ('Você escolheu sair do programa!')
        break
if 5 in b:
    print ('O valor 5 foi digitado!')
else:
    print ('O valor 5 não foi digitado')
b.sort(reverse=True)
print (f'Você digitou um total de {c} numeros\nOs numeros ao inverso são: {b}')