import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
# caso uso o import apenas de radians, sin, cos, tan ficaria assim: seno = sin(radians(angulo))
cosseno = math.cos(math.radians(angulo))
# caso uso o import apenas de radians, sin, cos, tan ficaria assim: cosseno = cos(radians(angulo))
tangente = math.tan(math.radians(angulo))
# caso uso o import apenas de radians, sin, cos, tan ficaria assim: tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}\n'
      f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}\n'
      f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')
