# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

cont = ''
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {extenso[n]}')
        while True:
            cont = input('Deseja continuar? [S/N] ').upper().strip()[0]
            if cont in 'SN':
                break
    else:
        print('Tente novamente. ', end='')
    if cont == 'N':
        break

# print(f'Você digitou o número {extenso[n]}')
