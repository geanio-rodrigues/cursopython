# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# jogador = dict()
# jogador['Nome'] = input('Nome do Jogador: ')
# partidas = int(input(f'     Quantas partidas {jogador['Nome']} jogou? '))
# total = 0
# gols = []
# for i in range(0, partidas):
#     gol = int(input(f'Quantos gols na {i+1}ª partida? '))
#     gols.append(gol)
#     total += gol
# jogador['Gols'] = gols
# jogador['Total'] = total
# print('=' * 60)
# print(jogador)
# print('=' * 60)
# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}')
# print('=' * 60)
# print(f'O jogador {jogador['Nome']} jogou {partidas} Partidas.')
# p = 1
# for i in jogador['Gols']:
#     print(f'    => Na Partida {p}, fez {i} Gols.',)
#     p += 1
# print(f'Foi um total de {jogador['Total']} Gols.')

# Método em aula:

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas o {jogador['nome']} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols.')
