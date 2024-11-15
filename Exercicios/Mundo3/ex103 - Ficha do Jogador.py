# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha(nome, gol):
    if nome == '':
        nome = '<desconhecido>'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


# Programa principal
print('-' * 30)
jogador = input('Nome do Jogador: ')
gols = input('Número de Gols: ')
ficha(jogador, gols)
