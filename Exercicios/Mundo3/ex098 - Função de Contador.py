# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize
# a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada.

from time import sleep


def contador(i, f, c):
    if c < 0:
        c = -c
    if c == 0:
        c = 1
    print(f'Contagem de {i} até {f} de {c} em {c}')
    if i < f:
        while i <= f:
            sleep(0.5)
            print(i, end=' ')
            i += c
    elif i > f:
        while i >= f:
            sleep(0.5)
            print(i, end=' ')
            i -= c
    sleep(0.5)
    print('Fim!')
    print('-=' * 20)


# Programa principal
print('-=' * 20)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
print('-=' * 20)
contador(inicio, fim, passo)
