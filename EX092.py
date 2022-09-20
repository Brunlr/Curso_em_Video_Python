a= dict()
a['nome'] = str(input('Digite seu nome: '))
a['nascimento'] = int(input('Digite seu ano de nascimento: '))
a['idade'] = 2022-a['nascimento']
a['ctps'] = int(input('Digite o numero de sua carteira de trabalho: (Se não possuir digite 0)'))

if a['ctps']!=0:
    a['ano de contratacao'] = int(input('Digite seu ano de contratação: '))
    a['aposentadoria'] = (a['ano de contratacao']+35)-a['nascimento']
    a['salario'] = float(input('Digite seu salario: '))
for b,c in a.items():
    print (f'O campo {b} tem valor {c}')
