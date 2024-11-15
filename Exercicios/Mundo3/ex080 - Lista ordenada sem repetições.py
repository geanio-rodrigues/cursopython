# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção(sem usar o sort()).
# No final, mostre a lista ordenada na tela.

# Tentativa de refazer depois de assistir a aula de resolução
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[c-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        for i in range(0, len(lista)+1):
            if len(lista) > c:
                break
            elif n <= lista[i]:
                lista.insert(i, n)
                print(f'Adicionado na posição {i} da lista...')
print('-=' * 30)
print(f'Os valores digitados foram: {lista}')

# Não consegui resolver tudo. Método resolvido em aula:

# lista = []
#
# for c in range(0, 5):
#     n = int(input('Digite um valor: '))
#     if c == 0 or n >= lista[-1]:
#         lista.append(n)
#         print('Adicionado ao final da lista...')
#     else:
#         pos = 0
#         while pos < len(lista):
#             if n <= lista[pos]:
#                 lista.insert(pos, n)
#                 print(f'Adicionado na posição {pos} da lista...')
#                 break
#             pos += 1
# print('-=' * 30)
# print(f'Os valores digitados foram: {lista}')
