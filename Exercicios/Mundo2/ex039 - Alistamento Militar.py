# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar. Se é a hora de se alistar. Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

sexo = input('Informe seu Sexo (F/M): ').strip()
ano_nascimento = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if sexo.upper() == 'M':
    if idade < 18:
        if idade == 17:
            print('Você terá que fazer o Alistamento Militar no ano que vem!')
        else:
            print(f'Você terá que fazer o Alistamento Militar daqui a {18 - idade} anos!')
    elif idade == 18:
        print('Você deve procurar a junta militar para realizar seu Alistamento Militar esse ano.')
    else:
        if idade == 19:
            print('Você já passou da hora, deveria ter feito o Alistamento Militar no ano passado')
        else:
            print(f'Você já passou da hora, deveria ter feito o Alistamento Militar a {idade - 18} anos atrás!')
elif sexo.upper() == 'F':
    print('Você não é obrigada a fazer o Alistamento Militar!')
else:
    print('Oops!! Alguma opção foi digitada errada! Tente Novamente!')
print('Encerrando...')
