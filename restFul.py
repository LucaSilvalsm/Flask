from flask import Flask, request
from flask_restful import Resource, Api
from habilidade import Habilidade, ListaHabilidade, CriarHabilidade
import json 

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Lucas',
        'sobrenome': 'Moreira',
        'Habilidade': 'CSS-HTML-Python-MYSQL-PHP-Laravel-NODE.JS',
        'Atuação': 'Back-end'
    },
    {
        'id': 1,
        'nome': 'Matheus',
        'sobrenome': 'Machado',
        'Habilidade': 'CSS-HTML-REACT-ANGULAR-SAAS',
        'Atuação': 'Front-end'
    },
    {
        'id': 2,
        'nome': 'Guilherme',
        'sobrenome': 'Monteiro',
        'Habilidade': 'AWS-CLOUD-PYTHON-MYSQL-NOSQL-R-',
        'Atuação': 'Data Science'
    },
    {
        'id': 3,
        'nome': 'Rafael',
        'sobrenome': 'Silva',
        'Habilidade': 'CSS-HTML-Python-PHP-REACT-ANGULAR',
        'Atuação': 'Full-Stack'
    }
]

class Desenvolvedor(Resource):

    def get(self, id):
        for dev in desenvolvedores:
            if dev['id'] == id:
                return dev
        return {'mensagem': 'Desenvolvedor não encontrado'}, 404

    def put(self, id):
        dados_json = request.get_json()

        # Verifica se o desenvolvedor com o ID existe na lista
        if id < 0 or id >= len(desenvolvedores):
            return {'erro': 'Desenvolvedor não encontrado'}, 404

        # Atualiza os dados do desenvolvedor na lista
        desenvolvedores[id].update(dados_json)

        return desenvolvedores[id], 200

    def delete(self, id):
        if id < 0 or id >= len(desenvolvedores):
            return {'erro': 'Desenvolvedor não encontrado'}, 404

        del desenvolvedores[id]
        return {'mensagem': 'Desenvolvedor deletado com sucesso!'}

class ListaDesenvolvedores(Resource):

    def get(self):
        return {'desenvolvedores': desenvolvedores}
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao], 201

# Adiciona os recursos à API com suas respectivas rotas
api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/desenvolvedores')
api.add_resource(Habilidade, '/habilidade/<int:id>')
api.add_resource(ListaHabilidade, '/habilidade/lista')
api.add_resource(CriarHabilidade, '/habilidade')

if __name__ == '__main__':
    app.run(debug=True)
