# Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: Use cores.

from time import sleep


def menu(msg, fim=False, manual=False):
    tam = len(msg) + 4
    if fim:
        print('\033[1;41m', end='')
        print(f'{'~' * tam}\n  {msg}\n{'~' * tam}')
        print('\033[m')
    elif manual:
        print('\033[1;46m', end='')
        print(f'{'~' * tam}\n  {msg}\n{'~' * tam}')
        print('\033[m', end='')
    else:
        sleep(1)
        print('\033[1;42m', end='')
        print(f'{'~' * tam}\n  {msg}\n{'~' * tam}')
        print('\033[m', end='')


def pyhelp(com):
    msg = 'Acessando o manual do comando ' + com
    menu(msg, manual=True)
    sleep(1)
    print('\033[7;40m', end='')
    print(help(com))
    print('\033[m', end='')


# Programa Principal
while True:
    menu('SISTEMA DE AJUDA PyHELP')
    resposta = input('Função ou Biblioteca > ').strip().lower()
    if resposta == 'fim':
        menu('ATÉ LOGO!', fim=True)
        break
    else:
        pyhelp(resposta)
