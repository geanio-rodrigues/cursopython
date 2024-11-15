# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais. Isósceles: dois lados iguais. Escaleno: todos os lados diferentes.

print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)

lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    print('Os segmentos acima PODEM FORMAR um triângulo!', end=' ')
    if lado1 == lado2 == lado3:
        print('E eles formam um triângulo EQUILÁTERO!')
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print('E eles formam um triângulo ISÓSCELES!')
    else:
        print('E eles formam um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

