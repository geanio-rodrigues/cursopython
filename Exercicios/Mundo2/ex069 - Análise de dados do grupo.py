# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer continuar ou não. No final, mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.

menu = 'CADASTRE UMA PESSOA'
cadastros = 0
mais_dezoito = 0
total_homens = 0
mulheres_menos_vinte = 0

while True:
    print('-' * 30)
    print(f'{menu:^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip()[0]
    print('-' * 30)
    cadastros += 1
    if idade >= 18:
        mais_dezoito += 1
    if sexo in 'Mm':
        total_homens += 1
    if sexo in 'Mm':
        if idade < 20:
            mulheres_menos_vinte += 1
    if sexo not in 'MmFf':
        decisao = 'DADOS INVÁLIDOS'
    elif idade < 0:
        decisao = 'DADOS INVÁLIDOS'
    else:
        decisao = input('Quer continuar? [S/N]').strip()[0]
    if decisao:
        if decisao in 'Nn':
            break
        elif decisao in 'Ss':
            continue
        else:
            print('Dados Inválidos. Cadastro excluído!\n'
                  'POR FAVOR INSIRA AS INFORMAÇÕES NOVAMENTE!')
            cadastros -= 1
            continue
print(f'\nTotal de pessoas com mais de 18 anos: {mais_dezoito}\n'
      f'Ao todo temos {total_homens} homens cadastrados\n'
      f'E temos {mulheres_menos_vinte} mulheres com menos de 20 anos')
