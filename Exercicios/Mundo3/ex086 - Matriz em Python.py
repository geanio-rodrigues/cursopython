# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formação correta

matriz = []
dados = []

for c in range(0, 3):
    dados.append(int(input(f'Digite um valor para [{c}, 0]: ')))
    dados.append(int(input(f'Digite um valor para [{c}, 1]: ')))
    dados.append(int(input(f'Digite um valor para [{c}, 2]: ')))
    matriz.append(dados[:])
    dados.clear()
print('-' * 50)
for n in matriz:
    print(f'[{n[0]:^5}][{n[1]:^5}][{n[2]:^5}]')

# Método resolvido em aula:

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-=' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()
