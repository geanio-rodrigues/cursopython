num = int(input('Informe um número: '))
print(f'Analisando o número {num}')
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f'Unidade: {unidade}\n'
      f'Dezena: {dezena}\n'
      f'Centena: {centena}\n'
      f'Milhar: {milhar}\n')
# Caso eu queria excluir os que aparecerem zerados, posso usar condição antes de mostrar o print dessa forma:
# if unidade > 0:
#     print(f'Unidade: {unidade}')
# if dezena > 0:
#     print(f'Dezena: {dezena}')
# if centena > 0:
#     print(f'Centena: {centena}')
# if milhar > 0:
#     print(f'Milhar: {milhar}')
