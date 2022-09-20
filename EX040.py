a = float(input('Digite sua primeira nota: '))
b = float(input('Digite sua segunda nota: '))
c = (a+b)/2 #media
if c>=7:
    print ('Situação final: APROVADO!')
elif c<=5:
    print ('Situação final: REPROVADO!')
else:
    print ('Situação final: RECUPERAÇÃO!')
print ('fim')