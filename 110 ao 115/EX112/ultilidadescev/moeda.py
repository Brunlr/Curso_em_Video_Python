def aumentar(a=0,num=0, formato = False):
    a = a + (a*(num/100))
    return a if formato is False else moeda(a)


def diminuir(a=0,num=0, formato = False):
    a = a - (a*(num/100))
    return a if formato is False else moeda(a)


def dobro(a=0, formato = False):
    a*=2
    return a if formato is False else moeda(a)


def metade(a=0, formato = False):
    a/=2
    return a if formato is False else moeda(a)


def moeda(preco=0, moeda='R$', formato = False):
    return f'{moeda}{preco:8.2f}'.replace('.',',')   #replace ponto no local da virgula


def resumo(preço = 0,taxaa=10,taxar=5):
    print ('-'*30)
    print ('RESUMO DO VALOR'.center(30))
    print ('-'*30)
    print (f'Preço analisado: \t{moeda(preço)}')
    print (f'Dobro do preço: \t{dobro(preço, True)}')
    print (f'Dobro do preço: \t{metade(preço, True)}')
    print (f'Com {taxaa}% de aumento: {aumentar(preço,taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço,taxar,True)}')
    print ('-'*30)
