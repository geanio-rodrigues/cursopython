preco = float(input('Qual é o preço do produto? R$'))
desconto = 0.05 * preco
preco_final = preco - desconto
print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${preco_final:.2f}')
