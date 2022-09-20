a = list()
b = 0 #recebe valor
c = 0 #maior numero
d = 0 #menor numero
for e in range(0,5):
    b = int(input(f'Digite um valor para posição {e}: '))
    a.append(b)
    if d==0:
        d = b
    elif d>b:
        d=b
    if b>c:
        c = b
print (f'Você digitou os valores {a}\nO maior valor digitado foi o {c} na posção {a.index(c)}\nO menor valor digitado foi o {d}, na posição {a.index(d)}')
