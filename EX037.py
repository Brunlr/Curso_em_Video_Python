num = int(input('Digite um numero inteiro: '))
print('Escolha um das bases para a conversao:\n1-Converter para BINARIO\n2-Converter para OCTAL\n3-Converter para HEXADECIMAL: ')
opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    print (f'{num} convertido para BINARIO é {bin(num)}')
elif opcao==2:
    print (f'{num} convertido para OCTAL é igual a {oct(num)}')
elif opcao ==3:
    print (F'{num} convertido para HEXADECIMAL é igual a {hex(num)}')
else:
    print ('Opção ivalida, tente novamente')
print('fim')