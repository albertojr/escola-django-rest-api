import requests


class TestCurso:
    headers = {'Authorization' : 'Token c4495f64785e06ca7a0ee960d01281047c9d9b85'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200
    
    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}6/', headers= self.headers)

        assert resposta.status_code == 200
    
    def test_post_curso(self):
        novo = {
            "titulo": "Curso de programação Ruby",
            "url" : "http://www.google.com.br"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data = novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']
    
    def test_put_curso(self):
        atualizado = {
            "titulo" : "Novo curso de Ruby",
            "url" : "http://www.seila.com.br"
        }

        respostas = requests.put(url=f'{self.url_base_cursos}6/',headers=self.headers, data = atualizado)

        assert respostas.status_code == 200
        assert respostas.json()['titulo'] == atualizado['titulo']


    def test_delete_curso(self):
        respostas = requests.delete(url=f'{self.url_base_cursos}6/',headers=self.headers)

        assert respostas.status_code == 204 and len(respostas.text) == 0
