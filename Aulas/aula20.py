def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')


def soma2(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


def contador(*num):
    # for valor in num:
    #     print(valor, end=' ')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números!')
    print('Fim')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa principal
# a = 4
# b = 5
# s = a + b
# print(s)
soma(4, 5)

# a = 8
# b = 9
# s = a + b
# print(s)
soma(8, 9)

# a = 2
# b = 1
# s = a + b
# print(s)
soma(a=2, b=1)

soma(b=4, a=1)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

soma2(5, 2)
soma2(2, 9, 4)
