a = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
b=0
while True:
    b = int(input('Digite um numero de 0 a 20: '))
    if b>=0 and 20>=b:
        break
    else:
        print('Erro! Digite novamente.')
print (f'Você escolheu o numero {a[b]}')