a = 0
b = 0  #menor
c = 0  #maior
d = 0  #media
e = 0  #condicional
f = 0  #numeros
while e==0:
    a = int(input('Digite um numero: '))
    d+=a
    f+=1
    if b==0:
        b = a
    elif b>a:
        b=a
    if a>c:
        c=a
    e = int(input('Digite "0" para continuar, se quiser interromper pressione qualquer tecla: '))
print (f'Você digitou {f} numeros\nA media ficou em {d/f}\nO maior numero foi o {c}\nE o menor numero foi o {b}')