salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    aumento = 0.10 * salario
    salario_final = salario + aumento
else:
    aumento = 0.15 * salario
    salario_final = salario + aumento
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario_final:.2f} agora.')
