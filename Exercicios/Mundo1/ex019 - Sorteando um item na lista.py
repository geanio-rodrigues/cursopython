import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(alunos)
# Usando o from random import choice: escolhido = choice(alunos)
print(f'O aluno escolhido foi {escolhido}')
