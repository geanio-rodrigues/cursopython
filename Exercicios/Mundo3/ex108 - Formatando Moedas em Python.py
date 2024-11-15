# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um
# valor monetário formatado.

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}\n'
      f'O Dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}\n'
      f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}\n'
      f'Reduzindo 13%, temos {moeda.moeda(moeda.aumentar(p, 13))}')
