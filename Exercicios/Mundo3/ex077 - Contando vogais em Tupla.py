# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')
for i in tupla:
    print(f'Na palavra {i.upper()} temos ', end='')
    for n in i:
        if n in 'aeiou':
            print(n, end=' ')
    print('')
