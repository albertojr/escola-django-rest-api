import requests

headers = {'Authorization' : 'Token c4495f64785e06ca7a0ee960d01281047c9d9b85'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos ,headers=headers)

#print(resultado.json())

#testando se o endpoint está correto
assert resultado.status_code == 200