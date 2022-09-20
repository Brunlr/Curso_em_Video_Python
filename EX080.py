a = list() #lista
b = 0 #valor recebido
c = 0 #variavel tempo
d = 0
while True:
    if c==5:
        break
    b = int(input('Digite um valor: '))
    c+=1
    if c==1 or c==2 and b>a[0] or c==3 and b>a[0] and b>a[1] or c==4 and b>a[1] and b>a[2] or c==5 and b>a[2] and b>a[3]:
        print ('Adicionado ao final da lista') #lista com todos os finais
        a.append(b)
    elif a[0] > b:
        print ('Adicionado na posição 0 da lista')
        a.insert(0,b)
    elif b > a[0] and a[1] > b:
        print ('Adicionado a posição 1 da lista')
        a.insert(1, b)
    elif b > a[1] and a[2] > b:
        print ('Adicionado a posição 2 da lista')
        a.insert(2, b)
    elif b > a[2] and a[3] > b:
        print ('Adicionado a posição 3 da lista')
        a.insert(3, b)
    elif b > a[3] and a[4] > b:
        print ('Adicionado a posição 4 da lista')
        a.insert(4, b)
print (f'Os valores digitados em ordem foram: {a}')