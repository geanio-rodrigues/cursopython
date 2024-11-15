# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas)
# print(pessoas['nome'], pessoas['idade'], pessoas['sexo'])
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# for k in pessoas.keys():
#     print(k)
# for k in pessoas.values():
#     print(k)
# del pessoas['sexo']
# pessoas['nome'] = 'Leandro'
# pessoas['peso'] = 98.5
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# brasil = []
# estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(estado1)
# print(estado2)
# print(brasil)
# print(brasil[0])
# print(brasil[1])
# print(brasil[0]['UF'])
# print(brasil[1]['sigla'])
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    # for v in e.values():
    #     print(v, end=' ')
    # print()
