# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM. Até 14 anos: INFANTIL. Até 19 anos: JUNIOR. Até 25 anos: SÊNIOR. Acima: MASTER.

from datetime import date

ano_nascimento = int(input('Informe o ano de nascimento do atleta: '))
mes_nascimento = int(input('Informe o mês de nascimento do atleta: '))
ano_atual = date.today().year
mes_atual = date.today().month

# Teste de idade, se nasceu em um mês superior ao mês atual, ainda fez aniversário esse ano
if mes_atual < mes_nascimento:
    idade = ano_atual - ano_nascimento - 1
else:
    idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos. Categoria: MIRIM!')
elif idade <= 14:
    print(f'O atleta tem {idade} anos. Categoria: INFANTIL!')
elif idade <= 19:
    print(f'O atleta tem {idade} anos. Categoria: JUNIOR!')
elif idade <= 25:
    print(f'O atleta tem {idade} anos. Categoria: SÊNIOR!')
else:
    print(f'O atleta tem {idade} anos. Categoria: MASTER!')
