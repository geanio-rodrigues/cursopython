# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO:
# 1 para binário, 2 para octal, 3 para hexadecimal.

numero = int(input('Informe um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão:
1 - Binário
2 - Octal
3 - Hexadecimal''')
base_conversao = int(input('Sua escolha: '))
if base_conversao == 1:
    conversao = bin(numero)[2:]  # Usando o 2: para que seja excluído o 0b que aparece na conversão de binário
    print(f'\nO número {numero} em Binário é: {conversao}')
elif base_conversao == 2:
    conversao = oct(numero)[2:]  # Usando o 2: para que seja excluído o 0o que aparece na conversão de Octal
    print(f'\nO número {numero} em Octal é: {conversao}')
elif base_conversao == 3:
    conversao = hex(numero)[2:]  # Usando o 2: para que seja excluído o 0x que aparece na conversão de hexadecimal
    print(f'\nO número {numero} em Hexadecimal é: {conversao}')
else:
    print('\nEscolha inválida! Tente novamente!')
print('\nEncerrando Programa...')
