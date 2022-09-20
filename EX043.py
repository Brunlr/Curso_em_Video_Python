a = float(input('Digite seu peso: '))
b = float(input('Digite sua altura: '))
imc = a/(b*b)
if 18.5>imc:
    print (f'Você está abaixo do peso! seu imc é de {imc}')
elif imc>18.5 and 25>imc:
    print (f'Você está no peso ideal! seu imc é de {imc}')
elif imc>25 and 30>imc:
    print (f'Você está com sobrepeso seu imc é de {imc}')
elif imc>30 and 40>imc:
    print (f'Você está em obesidade! seu imc é de {imc}')
elif imc>40:
    print (f'Você tem obesidade morbida! seu imc é de {imc}')
print ('fim')