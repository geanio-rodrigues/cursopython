def leiaDinheiro(msg):
    while True:
        valor = input(msg).strip()
        if valor.replace(',', '1').isdigit():
            valor = float(valor.replace(',', '.'))
            break
        elif valor.replace('.', '1').isdigit():
            valor = float(valor)
            break
        elif valor.isdigit():
            valor = float(valor)
            break
        else:
            print(f'\033[1;31mERRO: "{valor}" é um preço inválido!\033[m')
    return valor


def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        else:
            print(f'{'\033[1;31m'}{'ERRO! Digite um número inteiro válido.'}{'\033[m'}')
    return num
