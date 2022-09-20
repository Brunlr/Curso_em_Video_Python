a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero '))

if a > b and a>c:
    print (f'O maior numero é o {a}')
    if b>c:
        print (f'O menor numero é o {c}')
    else:
        print (f'O menor numero é o {b}')
if b> a and b>c:
    print (f'O maior numero é o {b}')
    if a>c:
        print (f'O menor numero é o {c}')
    else:
        print (f'O menor numero é o {a}')
if c>a and c>b:
    print (f'O maior numero é o {c}')
    if a>b:
        print (f'O menor numero é o {b}')
    else:
        print (f'O menor numero é o {a}')