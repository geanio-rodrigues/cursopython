lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# # print(len(lanche))
#
# # for comida in lanche:
# #     print(f'Eu vou comer {comida}')
#
# # for cont in range(0, len(lanche)):
# #     print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
#
# print('Comi pra caramba!')
#
# print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c), c.count(5), c.count(4), c.count(9))
print(c.index(2), c.index(5), c.index(5, 1))

# pessoa = ('Geanio', 31, 'M', 82.61)
# print(pessoa)
# del(pessoa)
# pessoa = 2
# print(pessoa)
