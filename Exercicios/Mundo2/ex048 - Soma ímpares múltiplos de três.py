# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram
# no intervalo de 1 até 500.

acumulador = 0
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        acumulador += 1
        soma += i
print(f'A soma de todos os {acumulador} valores solicitados é {soma}')

# for i in range(3, 500, 6):
#     print(i, end=' ')
# print('Fim!')
