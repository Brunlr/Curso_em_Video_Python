print('	\033[1;36mCadastro de pessoas \033[m')
a = list() #lista primeira
g = list() #lista para a fração
b = list() #lista source
c = 0 #nome
i = 0 #controle de for final
d = 0 #idade
e = 0 #pessoas cadastradas
f = 0 #variavel de controle
while True:
    e += 1
    c = str(input('Digite seu nome: '))
    a.append(c)
    d = float(input('Digite a seu peso: '))
    a.append(d)
    b.append(a[:])
    a.clear()
    while True:
        f = int(input('[ 1 ] Continuar\n[ 2 ] Encerrar: '))
        if f== 1 or f==2:
            break
    if f==2:
        break
f = e//2
b.sort()
for h in b:
    i+=1
    if f>i:
        print (f'As pessoas mais leves foram {h[0]} com {h[1]}kg')
    else:
        print (f'As pessoas mais pesadas foram {h[0]} com {h[1]}kg')
print (f'Ao todo, foram {e} pessoas cadastradas')
