# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

numeros = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('-=' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}\n'
      f'Os valores ímpares digitados foram: {numeros[1]}')

# Método resolvido em aula:

# núm = [[], []]
# valor = 0
# for c in range(1, 8):
#     valor = int(input(f'Digite o {c}o. valor: '))
#     if valor % 2 == 0:
#         núm[0].append(valor)
#     else:
#         núm[1].append(valor)
# print('-=' * 30)
# núm[0].sort()
# núm[1].sort()
# print(f'Os valores pares digitados foram: {núm[0]}')
# print(f'Os valores ímpares digitados foram: {núm[1]}')
