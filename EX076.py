a = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Caneta',22.30,'Livro',34.90)
b = 0
print ('-'*30)
print ('Listagem de preços')
print ('-'*30)
for c in range(0,len(a)):
    if c%2 ==0:
        print (f'{a[c]:.<30}',end = '')
    else:
        print (f'R${a[c]:>7.2f}')

