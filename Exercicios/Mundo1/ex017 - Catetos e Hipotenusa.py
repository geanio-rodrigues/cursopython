from math import hypot
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
# uma das formas de fazer usando import de raiz quadrada: hipotenusa = sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
# outra forma de fazer sem usar import: hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
# usando o import math apenas teria que usar assim: hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
