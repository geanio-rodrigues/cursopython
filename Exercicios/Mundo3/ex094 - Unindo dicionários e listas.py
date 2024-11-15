# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dado de cada pessoa um um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) Uma lista com todas as mulheres
# d) Uma lista com todas as pessoas com idade acima da média.

# cadastros = []
# pessoa = {}
# total_idade = 0
# while True:
#     pessoa['Nome'] = input('Nome: ').strip().capitalize()
#     while True:
#         pessoa['Sexo'] = input('Sexo: [M/F] ').strip()
#         if pessoa['Sexo'] in 'MmFf':
#             break
#         else:
#             print('ERRO! Por favor, digite apenas M ou F.')
#     pessoa['Idade'] = int(input('Idade: '))
#     while True:
#         resposta = input('Deseja continuar? [S/N] ')
#         if resposta in 'SsNn':
#             break
#         else:
#             print('ERRO! Responda apenas S ou N.')
#     cadastros.append(pessoa.copy())
#     total_idade += pessoa['Idade']
#     if resposta in 'Nn':
#         break
# media = total_idade / len(cadastros)
# print('=' * 60)
# print(f'- Ao todo temos {len(cadastros)} pessoas cadastradas.\n'
#       f'- A média de idade é de {media} anos.\n'
#       f'- As mulheres cadastradas foram: ', end='')
# for i in cadastros:
#     if i['Sexo'] in 'Ff':
#         print(f'{i['Nome']}', end='. ')
# print(f'\n- Lista das pessoas que estão acima da média: ')
# for i in cadastros:
#     if i['Idade'] > media:
#         print(f'    Nome = {i['Nome']}; Sexo {i['Sexo'].upper()}; Idade = {i['Idade']};')
# print('<< ENCERRANDO >>')

# Método em aula:

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p['nome']} ', end='')
print()
print(f'Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<< ENCERRANDO >>')
