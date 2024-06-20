from flask_restful import Resource
from flask import request

# Lista de habilidades (global para este exemplo)
lista_habilidade = ['PHP', 'Laravel', 'Java', 'Python', 'Javascript', 'React', 'C#']

class Habilidade(Resource):
    def get(self, id):
        if id >= 0 and id < len(lista_habilidade):
            return lista_habilidade[id]
        else:
            return {'mensagem': 'Habilidade não encontrada'}, 404
        
    def put(self, id):
        dados_json = request.get_json()

        # Verifica se o índice está dentro dos limites válidos da lista
        if id < 0 or id >= len(lista_habilidade):
            return {'erro': 'Habilidade não encontrada'}, 404

        # Atualiza a habilidade na lista
        lista_habilidade[id] = dados_json  # Atualiza o elemento da lista com o JSON recebido

        return lista_habilidade[id], 200    
    
    def delete(self, id):
        if id < 0 or id >= len(lista_habilidade):
            return {'erro': 'Habilidade não encontrada'}, 404

        del lista_habilidade[id]
        return {'mensagem': 'Habilidade deletada com sucesso!'}
    
class ListaHabilidade(Resource):
    def get(self):
        return lista_habilidade
    
class CriarHabilidade(Resource):
    def post(self):
        dados_json = request.get_json()

        # Verifica se o dado recebido é uma string
        if not isinstance(dados_json, str):
            return {'erro': 'Dados inválidos, deve ser uma string'}, 400

        # Adiciona o novo item à lista de habilidades
        lista_habilidade.append(dados_json)
        
        # Retorna o novo item adicionado e seu índice
        return {'id': len(lista_habilidade) - 1, 'habilidade': dados_json}, 201
