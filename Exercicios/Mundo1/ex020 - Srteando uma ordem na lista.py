from random import shuffle
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print('A ordem de apresentação será:\n'
      f'{alunos}')
