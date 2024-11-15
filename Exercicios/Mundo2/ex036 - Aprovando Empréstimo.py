# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o VALOR
# DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar. Calcule e mostre o valor da prestação mensal,
# sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# Recebendo as variáveis informadas pelo usuário
valor_casa = float(input('Qual o valor da casa que deseja financiar? R$'))
salario = float(input('Qual o seu salário mensal? R$'))
tempo_financiamento = int(input('O pagamento do empréstimo será feito em quantos anos? '))

quantidade_prestacoes = tempo_financiamento * 12
valor_prestacao = valor_casa / quantidade_prestacoes
valor_maximo_prestacao = 0.3 * salario
valor_minimo_prestacao = 0.05 * salario

if valor_maximo_prestacao < valor_prestacao:
    print('\n'
          'Infelizmente não poderemos aprovar o empréstimo nesse momento.\n'
          f'Com as condições informadas o valor ficaria em {quantidade_prestacoes}x de R${valor_prestacao:.2f}\n'
          f'Porém o valor máximo que sua proposta permite ter de parcela é R${valor_maximo_prestacao:.2f}.')
    print('Tente novamente com outra proposta!')
elif tempo_financiamento > 25:  # Condição adicional minha, valor total de 300 parcelas.
    print('\n'
          'Infelizmente não poderemos aprovar um empréstimo no momento.\n'
          'O prazo máximo são de 300 parcelas.')
    print('Tente novamente com outra proposta!')
elif valor_minimo_prestacao > valor_prestacao:  # Condição adicional minha, valor mínimo de prestação 5% do salário.
    print('\n'
          'Infelizmente não poderemos aprovar um empréstimo no momento.\n'
          f'Com as condições informados o valor da parcela ficaria de R${valor_prestacao:.2f}\n'
          f'Porém o valor mínimo que sua proposta permite ter de parcela é R${valor_minimo_prestacao:.2f}')
else:
    print('\n'
          'Seu empréstimo foi APROVADO com sucesso:\n'
          f'O financiamento terá um total de {quantidade_prestacoes} parcelas, no valor de R${valor_prestacao:.2f}')
print('\n'
      'Encerrando...')
