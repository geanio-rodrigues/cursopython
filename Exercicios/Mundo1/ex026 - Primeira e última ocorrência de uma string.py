frase = input('Digite uma frase: ').strip()
total_letras_a = frase.upper().count('A')
primeira_letra_a = frase.upper().find('A') + 1
ultima_letra_a = frase.upper().rfind('A') + 1
print(f'A letra A aparece {total_letras_a} vezes na frase.')
print(f'A primeira letra A apareceu na posição {primeira_letra_a}')
print(f'A última letra A apareceu na posição {ultima_letra_a}')
