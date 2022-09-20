def contador(i,f,p):
    from time import sleep
    print (f'Contando de {i} até {f} de {p} em {p}')
    if i>=f:
        while i>=f:
            if 0 > p:
                print(i, flush=True, end=' ')
                sleep(0.5)
                i += p
            elif p>0:
                print(i, flush=True, end=' ')
                sleep(0.5)
                i-=p
        print ()
    elif i<=f:
        while i<=f:
            print (i,flush=True,end=' ')
            sleep(0.5)
            i+=p
        print ()


def linha():
    print ('=-'*30)


linha()
contador(1,10,1)
linha()
contador(10,0,2)
linha()
print ('Agora é a sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
while c==0:
    c = 1
linha()
contador(a,b,c)
