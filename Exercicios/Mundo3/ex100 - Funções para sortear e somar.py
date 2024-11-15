# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.

from time import sleep
from random import randint


def sorteia():
    lista = []
    for c in range(0, 5):
        lista.append(randint(1, 10))
    return lista


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += i
    return soma


# Programa principal
lista = sorteia()
print('Sorteando 5 valores da lista:', end=' ')
for i in lista:
    sleep(0.5)
    print(i, end=', ')
print('PRONTO!')
print(f'Somando os valores pares de {lista}, temos {somaPar(lista)}')
