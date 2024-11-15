from math import trunc
num = float(input('Digite um valor: '))
inteiro = trunc(num)  # Também pode ser feito convertendo a variável num para inteiro: inteiro = int(num)
print(f'O valor digitado foi {num} e a sua porção inteira é {inteiro}')
