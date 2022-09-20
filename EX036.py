a= float(input('Digite o valor da casa: '))
b = int(input('Digite o valor do seu salario: '))
c = int(input('Digite a quantidade em anos, que você gostaria de parcelar: '))
d = a/(c*12) #valor da casa/parcelas = valor da parcela
if d>(b*0.3):
    print(f'EMPRESTIMO NEGADO! A parcela mensal de {d} excede 30% do seu salario')
else:
    print (f'EMPRESTIMO APROVADO! A parcela mensal ficará no valor de {d}')
print ('fim')