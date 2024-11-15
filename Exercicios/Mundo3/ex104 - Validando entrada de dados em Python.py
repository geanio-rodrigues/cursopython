# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Phyton,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')

def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        else:
            print(f'{'\033[1;31m'}{'ERRO! Digite um número inteiro válido.'}{'\033[m'}')
    return num


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
