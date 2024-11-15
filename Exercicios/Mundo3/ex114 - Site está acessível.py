# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado

import requests

try:
    resp = requests.get('http://pudim.com')
except requests:
    print(f'\033[1;31mO site Pudim não está acessível no momento!')
else:
    print(f'\033[1;35mConsegui acessar o site Pudim com Sucesso!')

