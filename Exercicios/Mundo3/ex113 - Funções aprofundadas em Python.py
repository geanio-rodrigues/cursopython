# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31m\nO usuário preferiu não digitar esse número.\033[m')
            return 0


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31m\nO usuário preferiu não digitar esse número.\033[m')
            return 0


# Programa principal
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real {real}')
