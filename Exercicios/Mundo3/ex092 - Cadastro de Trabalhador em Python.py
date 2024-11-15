# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

cadastro = dict()
cadastro['Nome'] = input('Nome: ')
ano_nascimento = int(input('Ano de Nascimento: '))
idade = date.today().year - ano_nascimento
cadastro['Idade'] = idade
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] > 0:
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = cadastro['Contratação'] - ano_nascimento + 35
print('=' * 50)
for k, v in cadastro.items():
    print(f'- {k} tem o valor {v}')

# Método em aula:

# from datetime import datetime
# dado = dict()
# dado['nome'] = str(input('Nome: '))
# nasc = int(input('Ano de Nascimento: '))
# dado['idade'] = datetime.now().year - nasc
# dado['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
# if dado['ctps'] != 0:
#     dado['contratação'] = int(input('Ano de Contratação: '))
#     dado['salário'] = float(input('Salário: R$'))
#     dado['aposentadoria'] = dado['idade'] + ((dado['contratação'] + 35) - datetime.now().year)
# print('-=' * 30)
# for k, v in dado.items():
#     print(f' - {k} tem valor {v}')
#