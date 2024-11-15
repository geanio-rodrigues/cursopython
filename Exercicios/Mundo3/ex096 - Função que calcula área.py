# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    return a


# Programa Principal
print('Controle de Terrenos')
print('--------------------')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno {largura}m x {comprimento}m é de {area(largura, comprimento)}m²')
