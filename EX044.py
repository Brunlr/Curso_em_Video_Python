a = float(input('Digite o preço do produto: '))
b = int(input('Digite a forma de pagamento de acordo com o numero:\n1- Dinheiro a vista ou cheque\n2-Cartão a vista ou parcelado: '))
if b==1:
    print (f'Você escolheu o método dinheiro ou cheque!\nForam concebidos 10% de desconto e seu produto fica no valor total de R${a*0.9}')
elif b==2:
    c = int(input('Você escolheu o metodo cartão!\nPara pagar a vista digite 1\nPara parcelar em duas vezes digite 2\nPara parcelar em 3x ou mais digite 3: '))
    if c==1:
        print(f'Você escolheu o metodo de pagamento a vista!\nForam concebidos 5% de desconto e seu produto fica no valor total de {a*0.95}')
    elif c==2:
        print (f'Você escolheu o metodo de parcelamento em 2 vezes!\nCada parcela ficará no valor de {a/2}\nE o produto no valor total de {a}')
    elif c==3:
        d = int(input('Digite a quantidade de parcelas que você gostaria: '))
        if 3>a:
            print ('ocorreu um erro! Reinicie o processo')
        else:
            e=a*1.2
        print(f'Você escolheu o parcelamento do valor de R${a} em {d} vezes, cada parcela fica no valor de R${e/d}\nE o produto no valor total de R${e}')
print ('fim')