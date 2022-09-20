a = list()
b = int(input('Digite o primeiro valor: '))
a.append(b)
b = int(input('Digite o segundo valor: '))
a.append(b)
c = 0 #menu
while c!=5:
    print('[1] Somar \n[2]Multiplicar\n[3]Maior\n[4]Novos Numeros\n[5] Sair do programa ')
    c = int(input('Digite sua opção: '))
    if c==1:
        print(F'Você escolheu SOMA! O resultado é {sum(a)}')
    elif c==2:
        print(f'Você escolheu MULTIPLICAÇÃO! O resultado é {a[0]*a[1]}')
    elif c==3:
        a.sort(reverse=True)
        print (f'Você escolheu verificar o maior numero!O numero é o {a[0]}')
    if c==4:
        b= int(input('Você escolheu adicionar novos numeros! Digite o novo numero:'))
        
print('fim')
