from ex115.lib.interface import *
from time import sleep


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        return True
    except FileNotFoundError:
        return False


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO ao tentar criar o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um ERRO ao tentar abrir o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO ao tentar abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao tentar escrever os dados!')
        else:
            sleep(1)
            print(f'Novo registo de {nome} adicionado.')
            a.close()
