# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {i}: ')))

print('=-' * 30)
print(f'Você digitou os valores {lista}\n'
      f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'→ {i}', end=' ')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'→ {i}', end=' ')

# Método aprendido em aula
# listanum = []
# maior = menor = 0
#
# for i in range(0, 5):
#     listanum.append(int(input(f'Digite um valor para a Posição {i}: ')))
#     if i == 0:
#         maior = menor = listanum[i]
#     else:
#         if maior > listanum[i]:
#             maior = listanum[i]
#         if menor < listanum[i]:
#             menor = listanum[i]
#
# print('=-' * 30)
# print(f'Você digitou os valores {listanum}\n'
#       f'O maior valor digitado foi {maior} nas posições ', end='')
# for i, v in enumerate(listanum):
#     if v == maior:
#         print(f'{i}... ', end='')
# print()
# print(f'O menor valor digitado foi {menor} nas posições ', end='')
# for i, v in enumerate(listanum):
#     if v == menor:
#         print(f'{i}... ', end='')
# print()
