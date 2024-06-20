from flask import Flask,request
from flask_restful import Resource, Api
from models import Pessoas,Atividade,db_session


app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, id):
        pessoa = db_session.query(Pessoas).filter_by(id=id).first()

        if pessoa:
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'sobrenome': pessoa.sobrenome,
                'idade': pessoa.idade
            }
            return (response), 200  # Retorna a resposta como JSON com código 200 (OK)
        else:
            return {'message': f'Pessoa com id {id} não encontrada'}, 404  # Retorna mensagem de erro com código 404
    
   
        
    
    def put(self,id):
        try:
            dados = request.get_json()
            pessoa = db_session.query(Pessoas).filter_by(id=id).first()

            if pessoa:
                pessoa.nome = dados.get('nome', pessoa.nome)
                pessoa.sobrenome = dados.get('sobrenome', pessoa.sobrenome)
                pessoa.idade = dados.get('idade', pessoa.idade)

                pessoa.save()

                response = {
                    'message': 'Pessoa atualizada com sucesso',
                    'id': pessoa.id,
                    'nome': pessoa.nome,
                    'sobrenome': pessoa.sobrenome,
                    'idade': pessoa.idade
                }
               
                return (response), 200  # Retorna a resposta como JSON com código 200 (OK)
                
            else:
                return {'message': f'Pessoa com id {id} não encontrada'}, 404  # Retorna mensagem de erro com código 404
        except Exception as e:
            db_session.rollback()
            return {'message': f'Erro ao atualizar pessoa: {str(e)}'}, 500  # Retorna mensagem de erro com código 500 em caso de exceção
        
    def delete(self,id):
        pessoa = db_session.query(Pessoas).filter_by(id=id).first()
        pessoa.delete()
        mensagem = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)
        return {'status':'sucesso', 'Mensagem': mensagem}
        

class ListaPessoa(Resource):
    def get(self):
        try:
            pessoas = db_session.query(Pessoas).all()
            lista_pessoas = []
            for pessoa in pessoas:
                pessoa_dict = {
                    'id': pessoa.id,
                    'nome': pessoa.nome,
                    'sobrenome': pessoa.sobrenome,
                    'idade': pessoa.idade
                }
                lista_pessoas.append(pessoa_dict)
            return (lista_pessoas), 200  # Retorna a lista de pessoas como JSON com código 200 (OK)
        except Exception as e:
            return {'message': f'Erro ao listar pessoas: {str(e)}'}, 500
        
class CriarPessoa(Resource):
    def post(self):
        try:
            dados = request.get_json()
            
            pessoa = Pessoas(nome=dados['nome'], sobrenome=dados['sobrenome'], idade=dados['idade'])
            pessoa.save()
            
            response = {
                'message': 'Pessoa Criada com sucesso',
                'id': pessoa.id,
                'nome': pessoa.nome,
                'sobrenome': pessoa.sobrenome,
                'idade': pessoa.idade
            }
            
            return (response), 201  # Retorna os dados da pessoa criada com código 201 (Created)
        
        except Exception as e:
            db_session.rollback()
            return {'message': f'Erro ao criar pessoa: {str(e)}'}, 500  # Retorna mensagem de erro com código 500 em caso de exceção
   
class ListaAtividade(Resource):
    def get(self):
        try:
            atividades = db_session.query(Atividade).all()
            lista_atividades = []
            for atividade in atividades:
                pessoa = db_session.query(Pessoas).filter_by(id=atividade.pessoa_id).first()
                atividade_dict = {
                    'id': atividade.id,
                    'pessoa': pessoa.nome if pessoa else 'Pessoa não encontrada',  # Verifica se a pessoa existe
                    'nomeAtividade': atividade.nomeAtividade
                }
                lista_atividades.append(atividade_dict)
            return (lista_atividades), 200  # Retorna a lista de atividades como JSON com código 200 (OK)
        except Exception as e:
            return {'message': f'Erro ao listar atividades: {str(e)}'}, 500
    def post(self):
        try:
            dados = request.json
            
            # Busca a pessoa pelo nome recebido nos dados da requisição
            pessoa = db_session.query(Pessoas).filter_by(nome=dados['pessoa']).first()
            
            if pessoa:
                # Cria a atividade associando à pessoa encontrada
                atividade = Atividade(nomeAtividade=dados['nomeAtividade'], pessoa_id=pessoa.id)
                atividade.save()
                
                # Agora busca novamente a atividade recém-criada para obter os dados completos
                atividade_criada = db_session.query(Atividade).filter_by(id=atividade.id).first()
                
                # Constrói a resposta com o nome da pessoa
                response = {
                    'id': atividade_criada.id,
                    'pessoa': pessoa.nome,  # Aqui está o nome da pessoa
                    'nomeAtividade': atividade_criada.nomeAtividade
                }
                
                return (response), 201  # Retorna os dados da atividade criada com código 201 (Created)
            else:
                return {'message': f'Pessoa com nome {dados["pessoa"]} não encontrada'}, 404
            
        except Exception as e:
            db_session.rollback()
            return {'message': f'Erro ao criar atividade: {str(e)}'}, 500

            
api.add_resource(Pessoa, '/pessoa/<int:id>/')
api.add_resource(ListaPessoa, '/pessoa/')
api.add_resource(CriarPessoa, '/pessoa/create/')
api.add_resource(ListaAtividade, '/atividade/')


if __name__ == '__main__':
    app.run(debug=True)
