from math import sqrt

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = sqrt(num)  # Também pode elevar o número a 1/2 para realizar a raiz quadrada, tipo: num ** (1/2)
print(f'O dobro de {num} é {dobro}.\n'
      f'O triplo de {num} é {triplo}\n'
      f'A raiz quadrada de {num} é {raiz:.2f}')
