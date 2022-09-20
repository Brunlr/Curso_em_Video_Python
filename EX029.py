a = int(input('Digite a velocidade: '))
if a>80:
    print (f'Você ultrapassou a velocidade maxima da via de 80Km/h e será multado no valor de R${float((a-80)*7)}')
else:
    print ('Velocidade Permitida!')

print ('FIM')