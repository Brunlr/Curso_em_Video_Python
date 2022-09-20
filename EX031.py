print ('Calculadora de Preços')
a = float(input('Digite a distancia da viagem: '))
b = 0
if a>200:
    b = a*0.45
    c = 0.45
else:
    b = a*0.50
    c = 0.5
print (f'O custo do transporte de sua viagem ficará no valor de R${b} com cada KM custando R${c}')