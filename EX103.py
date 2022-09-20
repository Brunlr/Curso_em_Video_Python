def ficha(a):
    if a.isalnum():
        print()
    else:
        a = '<desconhecido>'
    return a

a = str(input('Nome do jogador: '))
b = str(input('Numero de gols: '))
if b.isnumeric()==False:
    b =0
else:
    b=0
c = ficha(a)
print(f'O jogador {c} fez {b} gol(s) no campeonato')