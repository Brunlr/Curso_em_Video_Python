a = 0
b = 0
d = 0
for c in range(0,7):
    a = int(input('Digite o ano de nascimento: '))
    if 2004>=a:
        d+=1
    elif a>2003:
        b+=1

print (f'Ao todo são {b} pessoas menores de idade e {d} pessoas maiores de idade')