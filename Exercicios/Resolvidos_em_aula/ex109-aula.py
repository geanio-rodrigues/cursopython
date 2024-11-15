import moedaaula

p = float(input('Digite o preço: R$'))
print(f'A metade de {moedaaula.moeda(p)} é {moedaaula.metade(p, True)}')
print(f'O dobro de {moedaaula.moeda(p)} é {moedaaula.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedaaula.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moedaaula.diminuir(p, 13, True)}')
