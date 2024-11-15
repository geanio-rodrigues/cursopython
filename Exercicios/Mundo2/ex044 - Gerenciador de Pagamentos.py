# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE
# PAGAMENTO:
# À vista dinheiro/cheque: 10% de desconto. À vista no cartão: 5% de desconto. Em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% de juros

valor_normal = float(input('Qual o preço das compras? R$'))
print('''Utilize uma das opções abaixo para pagamento:
1 - Dinheiro / Cheque
2 - Cartão: À vista
3 - Cartão: Até 2x
4 - Cartão: 3x ou mais''')
forma_pagamento = int(input('Sua escolha: '))

if forma_pagamento == 1:
    desconto = valor_normal * 0.1
    valor_final = valor_normal - desconto
    print('Para essa forma de pagamento você terá 10% de desconto\n'
          f'O produto que custa R${valor_normal:.2f}, sairá por R${valor_final:.2f}')
elif forma_pagamento == 2:
    desconto = valor_normal * 0.05
    valor_final = valor_normal - desconto
    print('Para essa forma de pagamento você terá 5% de desconto\n'
          f'O produto que custa R${valor_normal:.2f}, sairá por R${valor_final:.2f}')
elif forma_pagamento == 3:
    parcela = valor_normal / 2
    print(f'Para essa forma de pagamento não temos desconto. O valor à pagar é R${valor_normal:.2f} em 2x de R${parcela:.2f}')
elif forma_pagamento == 4:
    quantidade_parcelas = int(input('Em quantas vezes deseja parcelar?'))
    acrescimo = valor_normal * 0.2
    valor_final = valor_normal + acrescimo
    parcela = valor_final / quantidade_parcelas
    print('Para essa forma de pagamento você terá um acréscimo de 20%\n'
          f'O produto que custa R${valor_normal:.2f}, sairá por R${valor_final:.2f}', end=' ')
    print(f'em {quantidade_parcelas}x de R${parcela:.2f}')
else:
    print('Escolha Incorreta! Tente novamente!')
print('Encerrando...')
