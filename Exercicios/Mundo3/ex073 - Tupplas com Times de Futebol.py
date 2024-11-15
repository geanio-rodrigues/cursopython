# Cie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados da tabela
# c) Uma lista com os times em ordem alfabética
# d) Em que posição na tabela está o tima do Fortaleza.

times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Atlético-PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos',
         'Goiás', 'Coritiba', 'América-MG')

print('-=' * 15)
print(f'Lista de times do Brasileirão 2023: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Fortaleza terminou na {times.index('Fortaleza')+1}ª posição')

# Outra forma de usar o print, usando formatação sem aspas, parêntesis e colchetes

# print('-=' * 15)
# print('Lista de times do Brasileirão 2023: ', end='')
# for t in times:
#     print(t, end='. ')
# print('')
# print('-=' * 15)
# print('Os 5 primeiros são: ', end='')
# for t in range(0, 5):
#     print(times[t], end='. ')
# print('')
# print('-=' * 15)
# print('Os 4 últimos são: ', end='')
# for t in range(16, 20):
#     print(times[t], end='. ')
# print('')
# print('-=' * 15)
# print(f'Times em ordem alfabética: ', end='')
# for t in sorted(times):
#     print(t, end='. ')
# print('')
# print('-=' * 15)
# print(f'O Fortaleza terminou na {times.index('Fortaleza')+1}ª posição')
