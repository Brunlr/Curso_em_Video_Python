c = dict()
c['nome'] = str(input('Nome: '))
c['media'] = float(input(f'Nota de {c["nome"]}: '))
if c['media']>=7:
    c["situacao"] = 'Aprovado'
else:
    c["situação"] = 'Reprovado'
print (f'O nome é igual a {c["nome"]}')
print (f'A média é igual a {c["media"]}')
print (f'A situação é igual a {c["situacao"]}')