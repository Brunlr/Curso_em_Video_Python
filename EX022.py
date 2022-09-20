a = str(input('Digite seu nome: '))
b = a.split()
print (f'Seu nome com todas as letras maiúsculas fica {a.upper()}\nCom todas as letras minúsculas fica {a.lower()}\nO total de letras é {len(a) - a.count(" ")}\nO primeiro nome tem o total de {len(b[0])} letras')