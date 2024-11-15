# Crie um programa que faço o computador jogar Jokenpô com você.
from random import choice
from time import sleep

computador = [0, 1, 2]
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
# Essa será a escolha do usuário
escolha = int(input('Qual é a sua jogada? '))
# Escolhendo aleatóriamente para o computador
escolha_computador = choice(computador)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

if escolha == 0:
    if escolha_computador == 0:
        print('-=' * 11)
        print('Computador jogou Pedra\n'
              'Jogador jogou Pedra')
        print('-=' * 11)
        print('EMPATE')
    elif escolha_computador == 1:
        print('-=' * 11)
        print('Computador jogou Papel\n'
              'Jogador jogou Pedra')
        print('-=' * 11)
        print('COMPUTADOR VENCE')
    else:
        print('-=' * 11)
        print('Computador jogou Tesoura\n'
              'Jogador jogou Pedra')
        print('-=' * 11)
        print('JOGADOR VENCE')
elif escolha == 1:
    if escolha_computador == 0:
        print('-=' * 11)
        print('Computador jogou Pedra\n'
              'Jogador jogou Papel')
        print('-=' * 11)
        print('JOGADOR VENCE')
    elif escolha_computador == 1:
        print('-=' * 11)
        print('Computador jogou Papel\n'
              'Jogador jogou Papel')
        print('-=' * 11)
        print('EMPATE')
    else:
        print('-=' * 11)
        print('Computador jogou Tesoura\n'
              'Jogador jogou Papel')
        print('-=' * 11)
        print('COMPUTADOR VENCE')
elif escolha == 2:
    if escolha_computador == 0:
        print('-=' * 11)
        print('Computador jogou Pedra\n'
              'Jogador jogou Tesoura')
        print('-=' * 11)
        print('COMPUTADOR VENCE')
    elif escolha_computador == 1:
        print('-=' * 11)
        print('Computador jogou Papel\n'
              'Jogador jogou Tesoura')
        print('-=' * 11)
        print('JOGADOR VENCE')
    else:
        print('-=' * 11)
        print('Computador jogou Tesoura\n'
              'Jogador jogou Tesoura')
        print('-=' * 11)
        print('EMPATE')
else:
    print('JOGADA INVÁLIDA')

# Outra forma mais resumida:

# from random import randint
# itens = ('Pedra', 'Papel', 'Tesoura')
# computador = randint(0, 2)
# print('''Suas opções:
# [ 0 ] PEDRA
# [ 1 ] PAPEL
# [ 2 ] TESOURA''')
# jogador = int(input('Qual é a sua jogada? '))
# print('-=' * 11)
# print(f'Computador jogou {itens[computador]} \n'
#       f'Jogador jogou {itens[jogador]}')
# print('-=' * 11)
# if computador == 0:
#     if jogador == 0:
#         print('EMPATE')
#     elif jogador == 1:
#         print('JOGADOR VENCE')
#     elif jogador == 2:
#         print('COMPUTADOR VENCE')
#     else:
#         print('JOGADA INVÁLIDA')
# elif computador == 1:
#     if jogador == 0:
#         print('COMPUTADOR VENCE')
#     elif jogador == 1:
#         print('EMPATE')
#     elif jogador == 2:
#         print('JOGADOR VENCE')
#     else:
#         print('JOGADA INVÁLIDA')
# elif computador == 2:
#     if jogador == 0:
#         print('JOGADOR VENCE')
#     elif jogador == 1:
#         print('COMPUTADOR VENCE')
#     elif jogador == 2:
#         print('EMPATE')
#     else:
#         print('JOGADA INVÁLIDA')
# else:
#     print('JOGADA INVÁLIDA')
