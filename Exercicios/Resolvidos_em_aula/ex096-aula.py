def area(larg, comp):
    a = larg * comp
    print(f'A ára de um terreno {larg}x{comp} é de {a}m².')


# Programa principal
print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
