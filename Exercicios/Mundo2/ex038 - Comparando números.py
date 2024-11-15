# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando uma mensagem na tela:
# O primeiro valor é maior. O segundo valor é maior. Não existe valor maior, os dois são iguais.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print('O Primeiro valor digitado é maior!')
elif num2 > num1:
    print('O Segundo valor digitado é maior!')
else:
    print('Não existe valor maior. Os números são iguais!')
