# Crie um programa que leia dois valores e mostre um menu na tela:
# 1 somar
# 2 multiplicar
# 3 maior
# 4 novos números
# 5 sair do programa
# Seu programa deverá realizada a operação solicitada em cada caso

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while True:
    print('    [ 1 ] Somar\n'
          '    [ 2 ] Multiplicar\n'
          '    [ 3 ] Informar o Maior\n'
          '    [ 4 ] Escolher Novos Números\n'
          '    [ 5 ] Sair do programa')
    condicao = int(input('>>>>> Qual é a sua opção? '))
    if condicao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
        print('=-=' * 10)
    elif condicao == 2:
        mult = n1 * n2
        print(f'O resultado de {n1} x {n2} é {mult}')
        print('=-=' * 10)
    elif condicao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
            print('=-=' * 10)
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
            print('=-=' * 10)
        else:
            print('Os dois números são iguais, não tem maior!')
            print('=-=' * 10)
    elif condicao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-=' * 10)
    elif condicao == 5:
        print('Finalizando...')
        print('=-=' * 10)
        sleep(1)
        break
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
        print('=-=' * 10)
print('Fim do Programa! Volte Sempre!')
