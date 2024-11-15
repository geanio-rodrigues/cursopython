import moedaaula

p = float(input('Digite o preço: R$'))
print(f'A metade de {moedaaula.moeda(p)} é {moedaaula.moeda(moedaaula.metade(p))}')
print(f'O dobro de {moedaaula.moeda(p)} é {moedaaula.moeda(moedaaula.dobro(p))}')
print(f'Aumentando 10%, temos {moedaaula.moeda(moedaaula.aumentar(p, 10))}')
