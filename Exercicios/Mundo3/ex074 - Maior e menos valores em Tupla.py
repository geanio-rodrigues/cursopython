# Crie um programa que vai gerar cinco números aleatórios e colocar numa tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
tupla = ([], )
n = randint(1, 10)
tupla[0].append(n)
# maior = menor = n
for i in range(0, 4):
    n = randint(1, 10)
    tupla[0].append(n)
    # if n >= maior:
    #     maior = n
    # if n <= menor:
    #     menor = n

print('Os valores sorteados foram: ', end='')
for n in tupla[0]:
    print(n, end=' ')
# Usando o método da aula, posso excluir a verificação de maior e menor, e escrever assim diretamente:
print(f'\nO maior valor sorteado foi {max(tupla[0])}\n'
      f'O menor valor sorteado foi {min(tupla[0])}')
# print(f'\nO maior valor sorteado foi {maior}\n'
#       f'O menor valor sorteado foi {menor}')

# Modo resolvido em aula:

# from random import randint
# numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
#            randint(1, 10),)
# print('Os valores sorteados foram: ', end='')
# for n in numeros:
#     print(f'{n} ', end='')
# print(f'\nO maior valor sorteado foi {max(numeros)}\n'
#       f'O menor valor sorteado foi {min(numeros)}')
