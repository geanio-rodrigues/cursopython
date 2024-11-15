# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até ele acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint
computador = randint(0, 10)  # Faz o computador "PENSAR"
print('Sou seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?')
tentativas = 0

# Enquanto o jogador não acerto o número o loop continua
while True:
    jogador = int(input('Qual é seu palpite? '))  # Jogador tenta adivinhar
    tentativas += 1
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez')
    else:
        break

# Mostrando o resultado e quantas tentativas
if tentativas == 1:
    print('Você está lendo minha mente? Acertou na primeira tentativa.')
else:
    print(f'Acertou com {tentativas} tentativas. Parabéns!')
