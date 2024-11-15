# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

print('=--=' * 10)
print(f'{'BANCO ET':^40}')
print('=--=' * 10)
notas_50 = notas_20 = notas_10 = notas_1 = 0
while True:
    valor = int(input('Que valor você quer sacar? R$'))
    while valor >= 50:
        valor -= 50
        notas_50 += 1
    while valor >= 20:
        valor -= 20
        notas_20 += 1
    while valor >= 10:
        valor -= 10
        notas_10 += 1
    while valor >= 1:
        valor -= 1
        notas_1 += 1
    if valor == 0:
        break
if notas_50 >= 1:
    print(f'Total de {notas_50} cédulas de R$50')
if notas_20 >= 1:
    print(f'Total de {notas_20} cédulas de R$20')
if notas_10 >= 1:
    print(f'Total de {notas_10} cédulas de R$10')
if notas_1 >= 1:
    print(f'Total de {notas_1} cédulas de R$1')
print('=--=' * 10, '\nVolte Sempre ao BANCO ET! Tenha um Bom dia!')
