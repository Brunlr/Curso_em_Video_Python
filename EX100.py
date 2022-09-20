


def somapar(a):
    d = 0
    b = list()
    for c in a:
        if c%2==0:
            b.append(c)
    for e in b:
        d +=e
    print ()
    print (f'A soma de todos os numeros pares é {d}')


def sorteia(a):
    from random import randint
    from time import sleep
    print ('Os numeros sorteados são: ', end=' ')
    for c in range(0,5):
        n = randint(1,10)
        a.append(n)
    for c in a:
        sleep(0.3)
        print (c,flush = True, end=' ')



a = list()
sorteia (a)
somapar(a)
