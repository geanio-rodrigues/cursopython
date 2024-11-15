# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# Abaixo de 18,5: Abaixo do peso. Entre 18,5 e 25: Peso ideal. 25 até 30: Sobrepeso. 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida.

peso = float(input('Informe o seu peso (em Kg): '))
altura = float(input('Informe sua altura (em M): '))
imc = peso / altura**2

if imc < 18.5:
    print(f'Seu IMC é: {imc:.1f}. Você está ABAIXO do peso!')
elif imc < 25:
    print(f'Seu IMC é: {imc:.1f}. Você está no seu PESO IDEAL!')
elif imc < 30:
    print(f'Seu IMC é: {imc:.1f}. Você está com SOBREPESO!')
elif imc < 40:
    print(f'Seu IMC é: {imc:.1f}. Você está com OBESIDADE!')
else:
    print(f'Seu IMC é: {imc:.1f}. Você está com OBESIDADE MÓRBIDA!')
