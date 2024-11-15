# Faça um programa que leia o peso de cinco pessoas. E no final, mostre qual foi o maior e o menor peso.

# Variáveis para armazenar qual o maior e o menor peso, e a qual pessoa ele pertence
maior_peso = 0
menor_peso = 0
pessoa_maior_peso = 0
pessoa_menor_peso = 0

# Recebendo o peso de 5 pessoas, e armazenando o maior e o menor, e também guardando que pessoa ele pertence
for i in range(1, 5):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    # Nessa parte atribuindo todas a variáveis a primeira pessoa, posso fazer os teste da segunda em diante
    if i == 1:
        maior_peso = peso
        menor_peso = peso
        pessoa_maior_peso = i
        pessoa_menor_peso = i
    # Continuando os teste para armazenar os dado
    else:
        if peso > maior_peso:
            maior_peso = peso
            pessoa_maior_peso = i
        if peso < menor_peso:
            menor_peso = peso
            pessoa_menor_peso = i

print('')  # Espaço entre a informações recolhidas e o resultado a ser exibido

# Exibindo na tela o resultado
print(f'O maior peso lido foi da {pessoa_maior_peso}ª pessoa: {maior_peso:.1f}Kg\n'
      f'O menor peso lido foi da {pessoa_menor_peso}ª pessoa: {menor_peso:.1f}Kg')
