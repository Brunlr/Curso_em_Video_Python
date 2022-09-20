a= 0
b = 0
d = 0
for c in range(1,6):
    a=float(input('Digite o seu peso: '))

    if a>b:
        b=a
    elif d==0:
        d=a
    elif d>a:
        d=a
print(f'O maior peso foi {b} e o menor peso foi {d}')