# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

for n in range(0, len(numeros)):
    if numeros[n] % 2 == 0:
        pares.append(numeros[n])
    else:
        impares.append(numeros[n])
pares.sort()
impares.sort()
print(f'\nOs números digitadores foram: {numeros}\n'
      f'Números pares = {pares}\n'
      f'Números ímpares = {impares}')

# Método em aula. Usa o for de forma diferente

# for v, i in enumerate(numeros):
#     if v % 2 == 0:
#         pares.append(v)
#     else:
#         impares.append(v)

