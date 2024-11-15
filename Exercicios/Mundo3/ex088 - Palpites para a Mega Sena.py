# Faça um programa que ajude um jogador da MEGA SENA a cria palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep

jogos = []
jogo = []
print('-' * 30)
print(f'{'JOGO NA MEGA SENA':^30}')
print('-' * 30)
sorteios = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, sorteios):
    cont = 0
    while cont <= 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            cont += 1
    jogos.append(jogo[:])
    jogo.clear()
print(f'=-=-=-=-= SORTEANDO {sorteios} JOGOS =-=-=-=-=')
c = 0
for j in jogos:
    j.sort()
    sleep(1)
    print(f'Jogo {c+1}: {j}')
    c += 1
print('=-=-=-=-=- < BOA SORTE! > -=-=-=-=-=')

# Método resolvido em aula

# from random import randint
# from time import sleep
# lista = list()
# jogos = list()
# print('-' * 30)
# print('      JOGA NA MEGA SENA      ')
# print('-' * 30)
# quant = int(input('Quantos jogos você quer que eu sorteie? '))
# tot = 1
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1
# print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
# for i, l in enumerate(jogos):
#     print(f'Jogo {i+1}: {l}')
#     sleep(1)
# print('-=' * 5, '< BOA SORTE >', '-=' * 5)
