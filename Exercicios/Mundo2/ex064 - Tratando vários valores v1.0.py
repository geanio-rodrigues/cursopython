# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o Flag)

# Usando opção de saída a cada novo número
# cont = 0
# saida = ''
# soma = 0
# while saida != '999':
#     n = int(input('Digite um número: '))
#     cont += 1
#     soma += n
#     saida = input('Digite 999 para sair ou qualquer tecla para continuar: ')
# print(f'No total foram digitados {cont} números e a soma entre eles foi: {soma}')

# Sem perguntar opção de saída
cont = 0
saida = 0
soma = 0
while saida != 999:
    saida = int(input('Digite um número [999 para encerrar]: '))
    cont += 1
    soma += saida
# Essa conta após o laço serve para que a contagem e a soma desconsiderem o último valor digitado, 999
cont -= 1
soma -= saida

# Tratamento para digitação de apenas um número
if cont == 1:
    print(f'Foi digitado apenas o número {soma}')
elif cont == 0:
    print('Você digitou 999 para encerrar o programa!')
else:
    print(f'No total foram digitados {cont} números e a soma entre eles foi: {soma}')
print('Fim')
