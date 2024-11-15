distancia = float(input('Informe uma distância em metros: '))
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000
print(f'A medida de {distancia}m corresponde a:\n'
      f'{km}km\n'
      f'{hm}hm\n'
      f'{dam}dam\n'
      f'{dm:.0f}dm\n'
      f'{cm:.0f}cm\n'
      f'{mm:.0f}mm')
