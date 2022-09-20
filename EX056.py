a = 0 #nome
b = 0 #idade
c = 0 #sexo
d = 0 #homem mais velho
f = 0 #idade do homem mais velho
e = 0 #mulheres com menos de 20 anos
g = 0 #media de idade
for m in range(1,5):
    a = str(input('Digite o nome: '))
    b = int(input('Idade: '))
    c = int(input('Sexo:\n1- Masculino\n2-Feminino: '))
    if c==2 and b<20:
        e+=1
    elif c==1 and b>f:
        f=b
        d=a
    g +=b
print (f'Há {e} mulheres com menos de 20 anos.\nO homem mais velho é o {d} com {f} anos.\nA media de idade é {g//4}')