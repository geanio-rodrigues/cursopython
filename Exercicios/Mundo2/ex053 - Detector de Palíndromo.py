# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

# Recebendo a frase e deixando junto e sem espaços
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()  # Todas as palavras da frase serão separadas
tudo_junto = ''.join(palavras)  # Juntando as palavras sem espaço entre elas

# Invertendo a ordem do texto
inverso = ''  # variável para armazenar a frase ao contrário
for letra in range(len(tudo_junto) - 1, -1, -1):
    inverso += tudo_junto[letra]

# Mostrando ao usuário a frase junta e sem espaços, e a frase invertida
print(f'O inverso de {tudo_junto} é {inverso}')

# Teste para verificar se a frase digitada é ou não palíndromo
if tudo_junto == inverso:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitara não é um palíndromo!')
