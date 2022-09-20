def maior(lst):
    print('=-' * 30)
    from time import sleep
    print ('Analisando os valores passados...')
    sleep(1)
    maior = 0
    for c in lst:
        sleep(0.5)
        if c>maior:
            maior = c
        print (c,flush=True, end=' ')
    print(f'Foram informados {len(lst)} ao todo.')
    print(f'O maior valor foi o {maior}.')




c = [2,9,4,5,7,1]
maior(c)
c.clear()
c = [4,7,0]
maior(c)
c.clear()
c = [1,2]
maior(c)
c.clear()
c = [6]
maior(c)
c.clear()
c = []
maior(c)


# a = list()
# b = 0 #Condicional
# print ('Digite varios valores para saber o maior')
# while True:
#     a.append(int(input('Digite um valor: ')))
#     b = str(input('Deseja continuar? [S/N]')).upper()
#     if b=='N':
#         break
# print ('=-'*30)
# maior(a)
#
