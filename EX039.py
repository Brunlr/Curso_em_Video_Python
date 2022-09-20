a = int(input('Digite a sua data de nascimento: '))
b = 2022-a
if b == 18:
    print ('Você ja possuí 18 anos completos, está na hora de se alistar!')
elif b>18:
    print (f'Você tem {b} anos e já se passaram {b-18} anos para você se alistar!')
else:
    print (f'Você tem {b} anos e ainda faltam {18-b} anos para você se alistar')

print ('FIM')