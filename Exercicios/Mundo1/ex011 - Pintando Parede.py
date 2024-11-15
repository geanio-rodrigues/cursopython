largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área de {area}m².\n'
      f'Para pintar essa parede, você precisará de {tinta}l de tinta.')
