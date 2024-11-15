# a = ['banana', 1, 0.5, True, ['pera', 'uva'], 'morango']
# print(a[4])
# print(a[:4])
# print(a[:])
# print(a[2:])
# print(a[-1])
# print(a[-5]

minha_lista = []
n = 1
while n <= 5:
    numero = int(input(f'Digite o {n}º número: '))
    minha_lista += [numero]
    n += 1

print(minha_lista)


