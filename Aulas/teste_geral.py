# texto = input('Digite: ').strip()[0]
# if texto in 'SsNn':
#     print('Deu certo')
# else:
#     print('Vamos de novo')
# lista = [5, 9, 3, 7]
# # lista.sort()
# # print(f'em ordem {lista}')
# lista.insert(0, 2)
# print(lista)
# print(lista.count(2))
#
# lista = [[1,2,3],[4,5,6],[7,8,9]]
# soma = 0
# for n in lista:
#     print(n[2])
    # print(n[2])
    # for i in n:
    #     if i % 2 == 0:
    #         print(i)

# import random
# lista = []
# cont = 0
# while cont <= 6:
#     n = random.randint(1, 60)
#     if n not in lista:
#         lista.append(n)
#         cont += 1
# print(lista)

# jogadores = [{'Jogador': 'Ronaldinho', 'Gols': [2, 3, 2], 'Total': 7},
#              {'Jogador': 'Kaká', 'Gols': [3], 'Total': 3},
#              {'Jogador': 'Vampeta', 'Gols': [0, 0, 2, 2], 'Total': 4}]
# print(jogadores[1]['Gols'][0])
# print(jogadores[1]['Jogador'])

# def menu(msg, fim=False):
#     tam = len(msg) + 4
#     print(f'{'\033[7;40m'}{'~'*tam}\n  {msg}\n{'~'*tam}\n{'\033[m'}')
#
# menu('ATÉ LOGO!')

variavel = 1354
print('\033[7;40m', end='')
print('Texto 1')
print('Texto 2')
print(help(int))
print(variavel)
print('\033[m', end='')
print('Texto 3')