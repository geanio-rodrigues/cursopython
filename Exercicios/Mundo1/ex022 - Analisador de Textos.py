nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
maiusculas = nome.upper()
minusculas = nome.lower()
tamanho = len(nome) - nome.count(' ')
primeiro_nome = nome.split()
tamanho_primeiro_nome = len(primeiro_nome[0])
print(f'Seu nome em maiúsculas é {maiusculas}\n'
      f'Seu nome em minúsculas é {minusculas}\n'
      f'Seu nome tem {tamanho} letras\n'
      f'Seu primeiro nome é {primeiro_nome[0]} e ele tem {tamanho_primeiro_nome} letras.')
