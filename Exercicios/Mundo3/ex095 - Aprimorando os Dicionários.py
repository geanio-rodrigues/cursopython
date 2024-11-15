# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
# detalhes de aproveitamento de cada jogador.


jogadores = []
jogador = {}
while True:
    print('-' * 30)
    jogador['Nome'] = input('Nome: ').strip().capitalize()
    partidas = int(input(f'Quantas partidas o {jogador['Nome']} jogou? '))
    gols_partida = []
    for c in range(1, partidas+1):
        gols_partida.append(int(input(f'    Quantos gols na {c}ª partida? ')))
    jogador['Gols'] = gols_partida[:]
    jogador['Total'] = sum(gols_partida)
    jogadores.append(jogador.copy())
    while True:
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if resposta in 'SN':
            break
        elif resposta == '':
            print('ERRO! Nada foi digitado! Por favor, digite S ou N.')
        else:
            print('ERRO! Digite apenas S ou N.')
    if resposta == 'N':
        break
print('=' * 60)
print(f'{'Cod':<5}{'Nome':<15}{'Gols':<15}{'Total':<20}')
print('-' * 50)
cod = 0
for j in jogadores:
    print(f'{cod:<5}{j["Nome"]:<15}{str(j["Gols"]):<15}{j["Total"]:<20}')
    cod += 1
print('-' * 50)
while True:
    escolha = int(input('Mostrar dado de qual jogador? (999 para sair) '))
    if escolha == 999:
        break
    elif escolha > len(jogadores):
        print(f'ERRO! Não existe Jogador com código {escolha}!')
        print('-' * 50)
    else:
        print(f' -- Levantamento do Jogador {jogadores[escolha]['Nome']}')
        for c in range(0, len(jogadores[escolha]['Gols'])):
            print(f'    No {c+1}º jogo fez {jogadores[escolha]['Gols'][c]} gols.')
        print('-' * 50)
print('<< VOLTE SEMPRE >>')

# Método da aula:

# time = list()
# jogador = dict()
# partidas = list()
#
# while True:
#     jogador.clear()
#     jogador['nome'] = str(input('Nome do Jogador: '))
#     tot = int(input(f'Quantas partidas o {jogador['nome']} jogou? '))
#     partidas.clear()
#     for c in range(0, tot):
#         partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
#     jogador['gols'] = partidas[:]
#     jogador['total'] = sum(partidas)
#     time.append(jogador.copy())
#     while True:
#         resp = str(input('Quer continuar? [S/N] ')).upper()[0]
#         if resp in 'SN':
#             break
#         print('ERRO! Responda apenas S ou N.')
#     if resp == 'N':
#         break
# print('-=' * 30)
# print('cod ', end='')
# for i in jogador.keys():
#     print(f'{i:<15}', end='')
# print()
# print('-' * 40)
# for k, v in enumerate(time):
#     print(f'{k:>3} ', end='')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('-' * 40)
# while True:
#     busca = int(input('Mostrar dado de qual jogador? (999 para parar)'))
#     if busca == 999:
#         break
#     if busca >= len(time):
#         print(f'ERRO! Não existe jogador com código {busca}')
#     else:
#         print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}')
#         for i, g in enumerate(time[busca]['gols']):
#             print(f'    No jogo {i+1} fez {g} gols.')
#     print('-' * 40)
# print('<< VOLTE SEMPRE >>')
