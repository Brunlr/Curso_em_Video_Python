a = int(input('Digite um numero para saber seu fatorial: '))
d = 0
b=a
# for c in range(a,0,-1):
#     if c!=a:
#         a = a * c
#     print (f'{c}',end = ' ')
#     if c != 1:
#         print ('x', end=' ')
# print (f'= {a}')
while b!=0:
    if b!=a:
        a = a * b
    print (f'{b}',end = ' ')
    if b != 1:
        print ('x', end=' ')
    b -= 1
print (f'= {a}')