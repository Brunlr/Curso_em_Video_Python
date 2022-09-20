a = ('Aprender', 'Programar','Linguagem','Python','Curso','Gratis','Estudar','Praticar','Trabalhar','Mercado','Programador','Futuro')
for c in a:
    c = c.upper()
    print (f'Na palavra {c} temos: ', end=' ')
    if 'A' in c:
        print ('a', end=' ')
    if 'E' in c:
        print ('e', end=' ')
    if 'I' in c:
        print ('i', end=' ')
    if 'O' in c:
        print ('o', end=' ')
    if 'U' in c:
        print ('u',end =' ')
    print (end='\n')
print ('Fim')