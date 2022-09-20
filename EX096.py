def area(a,b):
    c = a*b
    print(f'A área de um terreno {a}x{b} é de {c}m²')

print ('CONTROLE DE TERRENOS ')
a = int(input('Digite a largura do terreno: '))
b = int(input('Digite a altura do terreno: '))

area(a, b)