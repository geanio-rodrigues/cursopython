# Faça um programa que leia um número qualquer e mostre o seu fatorial
# ex: 5! = 5x4x3x2x1 = 120

n = int(input('Digite um valor para obter seu fatorial: '))
cont = n
fatorial = n
while cont > 1:
    fatorial = fatorial * (cont - 1)
    cont -= 1
print(f'{n}! = {fatorial}')

# Utilizando modulo importando da biblioteca math
# from math import factorial
# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {factorial}')

# Forma mostrada em aula
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
