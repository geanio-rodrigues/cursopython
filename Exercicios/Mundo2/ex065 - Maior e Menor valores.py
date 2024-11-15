# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

# Com essa primeira fórmula, fará com que maior, menor possam ser testados dentro do laço
n = int(input('Digite um número: '))
maior = n
menor = n
soma = n
cont = 1
escolha = input('Deseja continuar? [S/N]: ')
while escolha.upper() == 'S':
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont += 1
    escolha = input('Deseja continuar? [S/N]: ')
if cont == 1:
    print(f'Você digitou apenas o número {n}.')
else:
    media = soma / cont
    print(f'Foram digitador {cont} Números.\n'
          f'A média foi de: {media:.2f}\n'
          f'O maior número digitado foi: {maior}\n'
          f'O menor número digitado foi: {menor}')
