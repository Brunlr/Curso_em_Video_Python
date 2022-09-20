a = str(input('Digite uma frase: ')).upper()
print (f'Na palavra {a}, letra "A" aparece {a.count("A")} vezes na frase')
print (f'A primeira vez que a letra "A" aparece é na posição {a.find("A")+1}')
print(f'A ultima vez que a letra "A" aparece é na posição {a.rfind("A")+1}')