# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados
# b) A soma dos valores da terceira coluna
# c) O maior valor da segunda linha

matriz = []
dados = []
soma_par = soma_coluna = 0
for c in range(0, 3):
    dados.append(int(input(f'Digite um valor para [{c}, 0]: ')))
    dados.append(int(input(f'Digite um valor para [{c}, 1]: ')))
    dados.append(int(input(f'Digite um valor para [{c}, 2]: ')))
    matriz.append(dados[:])
    dados.clear()
print('-' * 50)
for n in matriz:
    print(f'[{n[0]:^5}][{n[1]:^5}][{n[2]:^5}]')
print('-' * 50)
for n in matriz:
    soma_coluna += n[2]
    for v in n:
        if v % 2 == 0:
            soma_par += v
print(f'A soma dos valores pares é {soma_par}\n'
      f'A soma dos valores da terceira coluna é {soma_coluna}\n'
      f'O maior valor da segunda linha é {max(matriz[1])}')

# Método resolvido em aula

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# spar = mai = scol = 0
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-=' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#         if matriz[l][c] % 2 == 0:
#             spar += matriz[l][c]
#     print()
# print('-=' * 30)
# print(f'A soma dos valores pares é {spar}')
# for l in range(0, 3):
#     scol += matriz[l][2]
# print(f'A soma dos valores da terceira coluna é {scol}')
# for c in range(0, 3):
#     if c == 0:
#         mai = matriz[1][c]
#     elif matriz[1][c] > mai:
#         mai = matriz[1][c]
# print(f'O maior valor da segunda linha é {mai}')
