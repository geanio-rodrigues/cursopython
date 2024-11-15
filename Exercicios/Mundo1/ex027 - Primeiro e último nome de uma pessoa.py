nome = input('Digite seu nome completo: ').strip().title()
nome_completo = nome.split()
primeiro_nome = nome_completo[0]
ultimo_nome = nome_completo[len(nome_completo)-1]
print('Muito prazer em te conhecer!\n'
      f'Seu primeiro nome é {primeiro_nome}\n'
      f'Seu último nome é {ultimo_nome}')
