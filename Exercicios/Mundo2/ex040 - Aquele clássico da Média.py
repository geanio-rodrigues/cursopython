# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final conforme
# a média atingida:
# Média abaixo de 5: REPROVADO. Média entre 5 e 6,9: RECUPERAÇÃO. Média 7 ou superior: APROVADO.

nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'A média do aluno foi {media:.1f}, e com essa média ele está REPROVADO!')
elif 5 <= media < 7:
    print(f'A média do aluno foi {media:.1f}, e com essa média ele está em RECUPERAÇÃO!')
else:
    print(f'A média do aluno foi {media:.1f}, e com essa média ele está APROVADO!')
