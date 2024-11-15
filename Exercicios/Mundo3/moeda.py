def aumentar(n, v, f=False):
    a = n + (n * (v / 100))
    if not f:
        return a
    else:
        return moeda(a)


def diminuir(n, v, f=False):
    d = n - (n * (v / 100))
    if not f:
        return d
    else:
        return moeda(d)


def dobro(n, f=False):
    d = n * 2
    if not f:
        return d
    else:
        return moeda(d)


def metade(n, f=False):
    m = n / 2
    if not f:
        return m
    else:
        return moeda(m)


def moeda(n):
    v = f'{n:.2f}'
    v = v.replace('.', ',')
    return f'R${v}'


def resumo(n, a, d):
    print(f'{'-'*40}\n{'RESUMO DE VALOR':^40}\n{'-'*40}')
    print(f'Preço analisado: \t\t\t{moeda(n)}\n'
          f'Dobro do preço: \t\t\t{dobro(n, True)}\n'
          f'Metade do preço: \t\t\t{metade(n, True)}\n'
          f'{a:02d}% de aumento: \t\t\t{aumentar(n, a, True)}\n'
          f'{d:02d}% de redução: \t\t\t{diminuir(n, d, True)}')
    print('-'*40)
