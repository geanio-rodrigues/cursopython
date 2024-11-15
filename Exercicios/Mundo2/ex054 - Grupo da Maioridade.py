# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas
# ainda não atingiram a maior idade e quantas já são maiores. (Considere a maior idade com 21 anos)

# Importação do date da biblioteca datetime para ler o ano atual
from datetime import date
ano_atual = date.today().year

# Variáveis para armazenar a quantidade de maiores e a quantidade de menores de idade
menor_idade = 0
maior_idade = 0

# Recebendo o ano de nascimento das 7 pessoas, e armazenando a informação de maior ou menos de idade
for i in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    if ano_atual - ano_nascimento >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print('')  # Usando essa linha apenas para dar espaço entre o final do laço e as informações abaixo

# Mostrando na tela a quantidade de maiores e menores de idade
# Fazendo o tratamento para não ter erro ortográfico (ex: 1 pessoas ou 0 pessoas), na hora de mostrar o resultado
if maior_idade == 0:
    print('Não tivemos nenhuma pessoa maior de idade. Todas as informadas são menores!')
elif menor_idade == 0:
    print('Não tivemos nenhuma pessoa menor de idade. Todas as informadas são maiores!')
else:
    if maior_idade == 1:
        print('Ao todo tivemos 1 pessoa maior de idade.')
    else:
        print(f'Ao todo tivemos {maior_idade} pessoas maiores de idade.')
    if menor_idade == 1:
        print('E também tivemos 1 pessoa menor de idade.')
    else:
        print(f'E também tivemos {menor_idade} pessoas menores de idade.')
