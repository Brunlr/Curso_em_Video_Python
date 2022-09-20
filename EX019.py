import random
a = str(input('Digite o nome do 1° aluno: '))
b = str(input('Digite o nome do 2° aluno: '))
c = str(input('Digite o nome do 3° aluno:'))
d = str(input('Digite o nome do 4° aluno: '))
e = [a,b,c,d]

print(f'O aluno escolhido para apagar o quadro foi {random.choice(e)}')
