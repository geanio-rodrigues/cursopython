# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos

print('=' * 30)
print('     10 TERMOS DE UMA PA')
print('=' * 30)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
termos = 0
while cont <= 10:
    print(f'{primeiro_termo}', end=' → ')
    primeiro_termo += razao
    cont += 1
    termos += 1

termo_seguinte = 1
while termo_seguinte != 0:
    print('PAUSA')
    termo_seguinte = int(input('Deseja mostrar mais quantos termos da PA? '))
    if termo_seguinte != 0:
        cont = 1
        while cont <= termo_seguinte:
            print(f'{primeiro_termo}', end=' → ')
            primeiro_termo += razao
            cont += 1
            termos += 1
print(f'Progressão finalizada com {termos} termos mostrados.')
