# Faça um programa que leia um número inteiro e diga se é ou não um número primo

numero = int(input('Digite um número: '))
numero_divisoes = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'{'\033[1;32m'}{c}{'\033[m'}', end=' ')
        numero_divisoes += 1
    else:
        print(f'{'\033[1;31m'}{c}{'\033[m'}', end=' ')
print('')  # essa linha apenas pra dar um espaço depois que mostrar todas as divisões
if numero_divisoes > 2:
    print(f'O número {numero} foi divisível {numero_divisoes} vezes\n'
          'E por isso ele NÃO É PRIMO!')
else:
    print(f'O número {numero} foi divisível {numero_divisoes} vezes\n'
          f'E por isso ele É PRIMO!')
