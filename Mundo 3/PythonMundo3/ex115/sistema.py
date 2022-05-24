from ex115.biblioteca.menu import *
from ex115.biblioteca.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Adicionar novas pessoas', 'Sair'])
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Digite o nome para cadastro: '))
        idade = leiaInt('Digite a idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('\033[31mSaindo do Sistema...\033[m')
        break
    else:
        cabecalho('\033[0;31mERRO! Digite uma opção válida\033[m')
    sleep(2)
