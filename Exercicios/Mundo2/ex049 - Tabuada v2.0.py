# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for

num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 13)
for i in range(1, 11):
    print(f'{num} x {i:2}  = {num*i:2}')
print('-' * 13)
