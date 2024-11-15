# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) Uma listagem com as pessoas mais pesadas
# c) Uma listagem com as pessoas mais leves

pessoas = []
dados = []
resposta = ' '
maior_peso = menor_peso = 0
while True:
    if resposta in 'Nn':
        break
    dados.append(input('Nome: ').strip().capitalize())
    dados.append(float(input('Peso: ')))
    if resposta == ' ':
        maior_peso = dados[1]
        menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while True:
        resposta = input('Deseja continuar? [S/N] ').strip()[0]
        if resposta in 'SsNn':
            break
        else:
            print('Digite S para sim e N para não!')
print('-=' * 40)
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')

# Método resolvido em aula:

# temp = []
# princ = []
# mai = men = 0
# while True:
#     temp.append(str(input('Nome: ')))
#     temp.append(int(input('Peso: ')))
#     if len(princ) == 0:
#         mai = men = temp[1]
#     else:
#         if temp[1] > mai:
#             mai = temp[1]
#         if temp[1] < men:
#             men = temp[1]
#     princ.append(temp[:])
#     temp.clear()
#     resp = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
# print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
# for p in princ:
#     if p[1] == mai:
#         print(f'[{p[0]}] ', end='')
# print()
# print(f'O menor peso foi de {men}Kg. Peso de ', end='')
# for p in princ:
#     if p[1] == men:
#         print(f'[{p[0]}] ', end='')
