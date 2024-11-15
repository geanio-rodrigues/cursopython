dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor_dia = 60 * dias
valor_km = 0.15 * km
valor_total = valor_dia + valor_km
print(f'O total a pagar é de R${valor_total:.2f}')
