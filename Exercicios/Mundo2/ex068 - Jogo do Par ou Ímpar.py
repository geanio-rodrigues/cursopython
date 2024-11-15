# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

menu = 'VAMOS JOGAR PAR OU ÍMPAR'
print('=-' * 15, f'\n{menu:^30}')
print('=-' * 15)

vitorias = 0

while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    par_impar = input('Par ou ìmpar? [P/I] ').strip()
    print('-' * 30)
    soma = computador + jogador
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR!')
        print('-' * 30)
        if par_impar in 'pP':
            print('Você VENCEU!')
            print('=-' * 15)
            vitorias += 1
        elif par_impar in 'Ii':
            print('Você PERDEU!')
            print('=-' * 15)
            break
        else:
            print('ESCOLHA APENAS P OU I. JOGADA ANULADA, TENTE NOVAMENTE.')
    else:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR!')
        print('-' * 30)
        if par_impar in 'Ii':
            print('Você VENCEU!')
            print('=-' * 15)
            vitorias += 1
        elif par_impar in 'Pp':
            print('Você PERDEU!')
            print('=-' * 15)
            break
        else:
            print('ESCOLHA APENAS P OU I. JOGADA ANULADA, TENTE NOVAMENTE.')
            print('=-' * 15)
if vitorias == 0:
    print('GAME OVER! Você não venceu nenhuma vez!')
elif vitorias == 1:
    print('GAME OVER! Você venceu apenas 1 vez!')
else:
    print(f'GAME OVER! Você venceu {vitorias} vezes.')
