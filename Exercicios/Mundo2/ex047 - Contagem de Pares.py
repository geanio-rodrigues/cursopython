# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
print('FIM')
# Com isso o programa vai roda 50 vezes, ou seja, 50 laços de repetição

for i in range(2, 51, 2):
    print(i, end=' ')
print('FIM')
# Dessa forma, usa menos o processador pois o programa vai rodar apenas 25 vezes, ou seja, 25 laços de repetição
