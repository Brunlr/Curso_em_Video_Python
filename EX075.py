a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))
d = int(input('Digite um numero: '))
e = (a,b,c,d)
g = 0 #numero 9
h = 0 #
i = list()
for f in e:
    if f==9:
        g+=1
    if f%2==0:
        i.append(f)
print (f'O valor 9 aparece {g} vezes\nO numero 3 foi digitado pela primeira vez na posição {e.index(3)+1}\nOs numeros pares foram os numeros:', end=' ')
for f in i:
    print (f,end=' ')
