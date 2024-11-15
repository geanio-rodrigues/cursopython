# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

numeros = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N] ').strip()[0]
    if continuar in 'Nn':
        break
numeros.sort(reverse=True)
print()
print(f'Foram digitados {len(numeros)} valores.\n'
      f'Listados de forma decrescente: {numeros}')
if numeros.count(5) == 0:
    print('O valor 5 não aparece na lista')
elif numeros.count(5) == 1:
    print(f'O valor 5 aparece 1 vez na posição {numeros.index(5)}')
else:
    print(f'O valor 5 aparece {numeros.count(5)} vezes. Nas posições ', end='')
    for i, v in enumerate(numeros):
        if v == 5:
            print(f'→ {i} ', end='')


