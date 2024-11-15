# Desenvolva um programa que leia seis número inteiros e mostre a soma apenas daqueles que forem pares
# Se o valor for ímpar, desconsidere-o

soma = 0
acumulador = 0
for c in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
        acumulador += 1
if acumulador == 1:
    print(f'Você informou apenas {acumulador} número par, o número foi: {soma}')
elif acumulador == 0:
    print('Não foi informado nenhum número Par!')
else:
    print(f'Foram informados {acumulador} números pares, e a soma deles é: {soma}')
