# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000
# Qual é o nome do produto mais barato.

barato = mais_mil = total = cont = 0
produto_barato = ''
print('-' * 40)
print(f'{'LOJA SUPER BARATÃO':^40}')
print('-' * 40)
while True:
    produto = input('Nome do Produto: ').strip()
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        mais_mil += 1
    if cont == 1 or preco < barato:
        barato = preco
        produto_barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^40}\n'
      f'O total da compra foi R${total:.2f}\n'
      f'Temos {mais_mil} produtos custando mais de R$1000.00\n'
      f'O produto mais barato foi {produto_barato} que custa R${barato:.2f}')
