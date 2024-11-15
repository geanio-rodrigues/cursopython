salario = float(input('Qual é o salário do Funcionário? R$'))
aumento = 0.15 * salario
salario_final = salario + aumento
print(f'Um Funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${salario_final:.2f}')
