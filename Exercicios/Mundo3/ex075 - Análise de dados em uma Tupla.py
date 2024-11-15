# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes o apareceu o valor 9
# b) Em que posição foi digitado o primeiro valor 3
# c) Quais foram os números pares

numeros = ([], )
for i in range(0, 4):
    n = int(input('Digite um número: '))
    numeros[0].append(n)

print(f'Os valores digitados foram: {numeros[0]}\n'
      f'O valor 9 apareceu {numeros[0].count(9)} vezes')
if 3 in numeros[0]:
    print(f'O valor 3 apareceu na {numeros[0].index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in numeros[0]:
    if n % 2 == 0:
        print(n, end=' ')

# Modo resolvido em aula:

# num = (int(input('Digite um número: ')),
#        int(input('Digite um número: ')),
#        int(input('Digite um número: ')),
#        int(input('Digite um número: ')))
# print(f'Você digitou os números {num}')
# print(f'O valor 9 apareceu {num.count(9)} vezes')
# if 3 in num:
#     print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
# else:
#     print('O valor 3 não foi digitado em nenhuma posição')
# print('Os valores pares digitados foram ', end='')
# for n in num:
#     if n % 2 == 0:
#         print(n, end=' ')
