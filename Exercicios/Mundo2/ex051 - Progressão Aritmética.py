# Desenvolva um program que leia o primeiro termo e a razão de uma PA (progressão aritmética)
# No final, mostre os 10 primeiros termos dessa progressão

print('=' * 30)
print('     10 TERMOS DE UMA PA')
print('=' * 30)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{c}', end=' → ')
print('ACABOU')
