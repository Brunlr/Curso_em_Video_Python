from math import hypot
a = float(input('Digite o comprimento do cateto adjacente: '))
b = float(input('Digite o comprimento do cateto oposto: '))
print (f'O comprimento da hipotenusa é igual a {(a**2+b**2)**0.5}')
hi = hypot(a,b)
# print (f'O comprimento da hipotenusa é igual a {hi}')