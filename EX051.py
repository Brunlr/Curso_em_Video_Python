from time import sleep
a=  int(input('Digite o numero que deseja iniciar a PA: '))
b = int(input('Digite a razão dessa PA: '))
for c in range(1,11):
    print (f'{c}- {a}')
    sleep(1)
    a+=b
print ('fim')