# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Fiz um procedimento parecido, mas no caso não se eu digitar ')()((x+1)' ele iria dar como correto.

# texto = input('Digite a expressão: ')
# inicio = texto.count('(')
# fim = texto.count(')')
# if inicio == fim:
#     print('Sua expressão está válida!')
# else:
#     print('Sua expressão está errada!')


# Método em aula

expressao = input('Digite a expressão: ')
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
