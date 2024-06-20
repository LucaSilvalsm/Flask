from flask import Flask, jsonify, request
import json 

app = Flask(__name__)
#API REST
# Lista de desenvolvedores
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

# Rota para listar todos os desenvolvedores
@app.route('/lista', methods=['GET'])
def lista():
    return jsonify(desenvolvedores)

# Rota para adicionar um novo desenvolvedor
@app.route('/adicionar', methods=['POST'])
def adicionar_desenvolvedor():
    novo_desenvolvedor = request.get_json()
    desenvolvedores.append(novo_desenvolvedor)
    return jsonify({'mensagem': 'Desenvolvedor adicionado com sucesso!'})

# Rota para deletar um desenvolvedor pelo ID
@app.route('/desenvolvedor/<int:id>', methods=['DELETE'])
def deletar_desenvolvedor(id):
    if id < 0 or id >= len(desenvolvedores):
        return jsonify({'erro': 'Desenvolvedor não encontrado'}), 404
    del desenvolvedores[id]
    return jsonify({'mensagem': 'Desenvolvedor deletado com sucesso!'})

# Rota para testar o servidor
@app.route('/testando', methods=['PUT'])
def testando():
    dados = json.load(request.data)
    desenvolvedores[id] = dados
    return jsonify(dados)

# Rota para obter um desenvolvedor pelo ID
@app.route('/desenvolvedor/<int:id>', methods=['GET'])
def obter_desenvolvedor(id):
    if id < 0 or id >= len(desenvolvedores):
        return jsonify({'erro': 'Desenvolvedor não encontrado'}), 404
    return jsonify(desenvolvedores[id])

if __name__ == "__main__":
    app.run()
