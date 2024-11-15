from lib.arquivo import *
from time import sleep

arq = 'Lista de Cadastros.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção que faz a listagem do conteúdo do arquivo criado
        sleep(1.5)
        lerArquivo(arq)
    elif resposta == 2:
        # Opção para cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção para sair do sistema.
        cabecalho('Saindo do Sistema... Até Logo!')
        break
    else:
        # Digitou uma opçDão errada no menu.
        print('\033[1;31mERRO! igite uma opção válida!')
    sleep(0.5)
