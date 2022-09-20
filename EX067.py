a= 0
b = 0
while True:
    a =  int(input('Digite um numero para saber a sua tabuada (Caso o numero for negativo será interrompido): '))
    if 0>a:
        break
    for c in range(1,11):
        print (f'{c}x{a} = {a*c}')
print ('fim')
