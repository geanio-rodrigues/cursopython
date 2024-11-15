# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogadores = {}
jogadas = []
for i in range(1, 5):
    jogadores['jogador'] = f'Jogador {i}'
    jogadores['jogada'] = randint(1, 6)
    jogadas.append(jogadores.copy())
print('Valores sorteados:')
for e in jogadas:
    sleep(1)
    print(f'    O {e["jogador"]} tirou {e["jogada"]} no dado.')
print('=' * 40)
print('Ranking dos jogadores:')
ranking = sorted(jogadas, key=lambda dicionario: dicionario['jogada'], reverse=True)
a = 1
for e in ranking:
    sleep(0.5)
    print(f'    {a}º Lugar: {e["jogador"]} com {e["jogada"]}.')
    a += 1

# Método em aula:

# from random import randint
# from time import sleep
# from operator import itemgetter
#
# jogo = {'jogador1': randint(1, 6),
#         'jogador2': randint(1, 6),
#         'jogador3': randint(1, 6),
#         'jogador4': randint(1, 6)}
# ranking = []
# print('Valores sorteados:')
# for k, v in jogo.items():
#     print(f'{k} tirou {v} no dado.')
#     sleep(1)
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print('-=' * 30)
# print('  == RANKING DOS JOGADORES ==')
# for i, v in enumerate(ranking):
#     print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
#     sleep(1)
