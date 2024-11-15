# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.

def notas(*n, sit=False):
    """
    → Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    aluno = {'Total': len(n), 'Maior': max(n), 'Menor': min(n)}
    media = sum(n)/len(n)
    aluno['Média'] = round(media, 1)
    if sit:
        if media >= 7:
            aluno['Situação'] = 'BOA'
        elif 5 < media < 7:
            aluno['Situação'] = 'RAZOÁVEL'
        else:
            aluno['Situação'] = 'RUIM'
    print('-' * 30)
    return aluno


# Programa principal
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
help(notas)
