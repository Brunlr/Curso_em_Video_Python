
a = 0 #idade
b = 0 #sexo
c = 0 #Pessoas com menos de 18
d = 0 #Quantos homem cadastrados
e = 0 #Quantas mulheres com menos de 20 anos
f = 0 #Condicional
while True:
    print('-' * 15)
    print('Cadastre uma pessoa')
    print('-' * 15)
    a = int(input('Idade: '))
    b = str(input('Sexo[M/F]: ')).upper()
    if b == "M":
        d +=1
    if 18>a:
        c+=1
    if 20>a and b=='F':
        e+=1
    else:
        print('Digite novamente')
    while True:
        f = str(input('Deseja continuar? [S/N]: ')).upper()
        if f=='S':
            break
        elif f=='N':
            break
    if f=='N':
        break
print (F'Ao todo temos:\n{c} Pessoas menores de idade\n{d} Homens cadastrados\n{e} Mulheres com menos de 20 anos')
