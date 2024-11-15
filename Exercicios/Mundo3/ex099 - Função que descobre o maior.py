# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    if len(num) > 0:
        for c in num:
            sleep(0.5)
            print(c, end=' ')
        print(f'Foram informados {len(num)} ao todo.\n'
              f'O maior valor informado foi {max(num)}')
    else:
        print('Nenhum valor foi informado.\n')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
