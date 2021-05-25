import requests

#GET Avaliacoes

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# print(avaliacoes.json())

#autenticação com request:
headers = {'Authorization' : 'Token c4495f64785e06ca7a0ee960d01281047c9d9b85'}

cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())