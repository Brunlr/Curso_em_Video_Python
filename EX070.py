
b = int()  #produtos +mil
c = 0 #total gastos
d = 0 #produto mais barato
e = 0 #condicional
g = 0 #nome do mais barato
a = 0 #nome do produto
f = 0 #Preço do produto
while True:
    a = str(input('Nome do Produto: '))
    f = float(input('Preço: '))
    c+=f
    if f>1000:
        b+=1
    if d ==0:
        d = f
        g = a
    if d>f:
        d=f
        g = a

    while True:
        e = int(input(f'Deseja continuar?\n[1] Sim\n[2] Não: '))
        if e==1 or e==2:
            break
        else:
            print ('Erro! Tente novamente')
    if e==2:
        break

print (f'O total gasto na compra foi R${c}\n{b} Produtos custam mais de R$1000,00\nO produto mais barato custa {d} e se chama {g}')