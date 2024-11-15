# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# Tentativa de refazer depois de assistir a aula de resolução
dados = []

while True:
    nome = input('Nome: ').strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], round(media, 1)])
    resp = input('Quer continuar? [S/N] ').strip()[0]
    if resp in 'Nn':
        break

print('-=' * 20)
print(f'{'Nº':<4} {'NOME':<10} {'MÉDIA':>8}')
print('-' * 25)
for i, a in enumerate(dados):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}')
print('-' * 25)

while True:
    print('-' * 25)
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    if aluno < len(dados):
        print(f'Notas de {dados[aluno][0]} são: {dados[aluno][1]}')
print('FINALIZANDO...\n'
      '<<< VOLTE SEMPRE >>>')

# Não consegui resolver tudo. Método resolvido em aula:

# ficha = list()
# while True:
#     nome = input('Nome: ')
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome, [nota1, nota2], media])
#     resp = input('Quer continuar? [S/N]')
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
# print('-' * 26)
# for i, a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# while True:
#     print('-' * 35)
#     opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if opc == 999:
#         print('FINALIZANDO...')
#         break
#     if opc <= len(ficha) - 1:
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
# print('<<< VOLTE SEMPRE >>>')
