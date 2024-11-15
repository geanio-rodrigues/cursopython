# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de uma pessoa, retornando
# um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import date


def voto(ano_nascimento):
    idade = date.today().year - ano_nascimento
    if idade < 16:
        situacao = 'NÃO VOTA'
    elif 18 <= idade <= 70:
        situacao = 'VOTO OBRIGATÓRIO'
    else:
        situacao = 'VOTO OPCIONAL'
    return idade, situacao


# Programa principal
print('-' * 40)
ano = int(input('Em que ano você nasceu? '))
print(f'Com {voto(ano)[0]} anos: {voto(ano)[1]}')
