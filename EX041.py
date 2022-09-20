a = int(input('Digite o ano de nascimento do atleta: '))
b = 2022 - a
if b<=9:
    print (f'Você possui {b} anos e está na categoria: MIRIM')
elif b>9 and b<=14:
    print(f'Você possui {b} anos e está na categoria:INFANTIL')
elif b>14 and b<=19:
    print (f'Você possui {b} anos e está na categoria: JUNIOR')
elif b==20:
    print (f'Você possui {b} anos e está na categoria: SENIOR')
else:
    print (f'Você possui {b} anos e está na categoria: MASTER')
print ('FIM')