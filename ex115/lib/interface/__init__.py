def linha(tam=40):
    return '-' * tam


def cabecalho(texto):
    print(linha())
    print(texto.center(40))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for p, item in enumerate(lista):
        print(f'\033[32m{p + 1}\033[m - \033[34m{item}\033[m')
    print(linha())
    opc = leiaInt('\033[35mSua Opção: \033[m')
    return opc


def leiaInt(msg):
    while True:
        try:
            resp = int(input(msg))
            return resp
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Por favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mERRO: Não foi digitado nenhum número!\033[m')
            return 0
