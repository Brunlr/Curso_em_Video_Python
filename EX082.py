a = list()
b = list()
c = list()
e = 0
d = int(input('Digite um numero (Digite 0 para encerrar): '))
while True:
    if d == 0:
        print ('Você escolheu encerrar o programa.')
        break
    a.append(d)
    d = int(input('Digite um numero:'))
for e in a:
    if e % 2 == 0:
        b.append(e)
    else:
        c.append(e)
print (f'Todos os valores digitados foram:\n{a}\nValores Pares: {b}\nValores Impares {c}')