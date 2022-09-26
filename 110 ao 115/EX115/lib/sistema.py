from EX115.lib.interface import *
from EX115.lib.Arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
print ('OI')
if not arquivoExiste(arq):
    criarArquivo(arq)

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    resposta  = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta ==1:
        #listar o conteudo
        lerArquivo(arq)
    elif resposta ==2:
        # cadastrar pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade:')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print ('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)