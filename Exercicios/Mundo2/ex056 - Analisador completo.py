# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

# Variáveis para armazenar as informações solicitadas acima
soma_idades = 0
mais_velho = 0
nome_mais_velho = ''
mulheres_menores_20 = 0

# Recebendo as informações de 4 pessoas e armazenando os dado solicitados
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    soma_idades += idade
    if sexo.upper() == 'M':
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome
    if sexo.upper() == 'F':
        if idade < 20:
            mulheres_menores_20 += 1

print('')  # Espaço entre as informações recolhidas e o resultado a ser exibido

# Calculando a média das idades
media = soma_idades / i

# Exibindo as informações solicitadas, com tratamento de erro ortográficos na exibição
if mulheres_menores_20 == 0:
    if mais_velho == 1:
        print(f'A média de idade do grupo é de {media:.1f} anos.\n'
              f'O homem mais velho tem {mais_velho} ano e se chama {nome_mais_velho.title()}\n'
              f'E não tem nenhuma mulher com menos de 20 anos.')
    else:
        print(f'A média de idade do grupo é de {media:.1f} anos.\n'
              f'O homem mais velho tem {mais_velho} anos e se chama {nome_mais_velho.title()}\n'
              f'E não tem nenhuma mulher com menos de 20 anos.')
elif mulheres_menores_20 == 1:
    if mais_velho == 1:
        print(f'A média de idade do grupo é de {media:.1f} anos.\n'
              f'O homem mais velho tem {mais_velho} ano e se chama {nome_mais_velho.title()}\n'
              f'E apenas 1 mulher com menos de 20 anos.')
    else:
        print(f'A média de idade do grupo é de {media:.1f} anos.\n'
              f'O homem mais velho tem {mais_velho} anos e se chama {nome_mais_velho.title()}\n'
              f'E apenas 1 mulher com menos de 20 anos.')
else:
    if mais_velho == 1:
        print(f'A média de idade do grupo é de {media:.1f} anos.\n'
              f'O homem mais velho tem {mais_velho} ano e se chama {nome_mais_velho.title()}\n'
              f'Ao todo são {mulheres_menores_20} com menos de 20 anos.')
    else:
        print(f'A média de idade do grupo é de {media:.1f} anos.\n'
              f'O homem mais velho tem {mais_velho} anos e se chama {nome_mais_velho.title()}\n'
              f'Ao todo são {mulheres_menores_20} com menos de 20 anos.')
