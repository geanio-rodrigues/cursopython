import moedaaula

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moedaaula.metade(p)}')
print(f'O dobro de R${p} é R${moedaaula.dobro(p)}')
print(f'Aumentando 10%, temos R${moedaaula.aumentar(p, 10)}')
