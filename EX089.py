a = list() #lista source
b = list() #lista primaria
f = 0 #condicional
g = 0 #numeração
c = 0 #nome
h = 0 #para o for no final
d = 0 #nota 1
i = 0 #contador
e = 0 #nota 2
while True:
    c = str(input('Digite seu nome: '))
    d = float(input('Digite sua primeira nota: '))
    e = float(input('Digite sua segunda nota: '))
    g += 1
    b.append(g)
    b.append(c)
    b.append(d)
    b.append(e)
    a.append(b[:])
    b.clear()
    while True:
        f = str(input('Deseja continuar? [S/N] ')).lower()
        if f=='s' or f=='n':
            break
    if f=='n':
        print('No.      NOME      MÉDIA')
        break
# print (f'{a} a , {g} g , {b} b')
for k in range(0,g):
    i=0
    for h in a[k]:

        if i == 2 or i==3:
            if i==2:
                b.append(h)
            if i==3:
                b.append(h)
                print (f'{b[1] + b[0]}', end='      ')
                b.clear()
                print(end='\n')
        else:
            print (f'{h}', end='      ')
        i+=1
    if i % 2 == 0 and i != 0:
        print(end='\n')

print (end='\n')
while True:
    g = int(input('Digite o numero da pessoa que você gostaria de ver as notas: (999 interrompe)'))
    if g==999:
        break
    print (f'Você escolheu o numero {a[g][0]} que seria {a[g][1]} e suas notas foram: {a[g][2]} e {a[g][3]}')