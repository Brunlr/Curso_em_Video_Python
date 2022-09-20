from time import sleep
times = ('Palmeiras','Flamengo', 'Corinthians','Fluminense','Athletico PR','Internacional','Atletico Mineiro','America MG','Chapecoense','Bragantino','Santos','São Paulo','Botafogo','Goias','Ceará','Fortaleza','Cuiaba','Avaí','Coritiba','Atletico Goianiense')
a = 0
b = list()
c = 0
while True:
    print ('-'*30)
    print ('             MENU             \n[1] Apenas os 5 primeiros colocados\n[2] Os ultimos 4 colocados\n[3] A lista de times por ordem alfabética\n[4] Em que posição está o Chapecoense\n[5] Sair do programa')
    print ('-'*30)
    a = int(input('Faça a sua escolha: '))
    if a==1:
        print (f'Você escolheu ver os 5 primeiros colocados! os times são :\n{times[:5]}')
        sleep(3)
    elif a==2:
        print (f'Você escolheu os ultimos 4 colocados! Os times são:\n{times[16:]}')
        sleep(3)
    elif a==3:
        b = ['Palmeiras','Flamengo', 'Corinthians','Fluminense','Athletico PR','Internacional','Atletico Mineiro','America MG','Chapecoense','Bragantino','Santos','São Paulo','Botafogo','Goias','Ceará','Fortaleza','Cuiaba','Avaí','Coritiba','Atletico Goianiense']
        b.sort()
        print (f'Os times em ordem alfabetica são:')
        for c in b:
            sleep(0.2)
            print (c)
        sleep(3)
    elif a==4:
        print (f'O Chapecoense está na posição {times.index("Chapecoense")+1}')
        sleep(3)
    elif a==5:
        print ('Você escolheu sair do programa!')
        sleep(3)
        break
    else:
        print ('Erro! Tente novamente..')
        sleep(1)
print ('Fim')
