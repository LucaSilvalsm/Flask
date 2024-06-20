from models import Pessoas, db_session

# Resto do seu código...


def insere_pessoas():
    pessoa = Pessoas(nome='Roberto', sobrenome='Braga', idade=45)
    db_session.add(pessoa)
    db_session.commit()
    print("Pessoa inserida:\n", pessoa)

def consulta():
    pessoas = db_session.query(Pessoas).all()  # Consulta todas as pessoas
    for pessoa in pessoas:
        print(pessoa)


def consultaId(id):
    pessoa = db_session.query(Pessoas).filter_by(id=id).first()
    if pessoa:
        print(pessoa)
    else:
        print(f"Pessoa com id {id} não encontrada.")

def altera_pessoa(id):
    pessoa = db_session.query(Pessoas).filter_by(id=id).first()
    if pessoa:
        pessoa.nome = 'Natasha'
        pessoa.sobrenome = 'Oliveira'
        pessoa.idade =  25
        db_session.commit()
        print("Pessoa alterada com sucesso.")
    else:
        print(f"Pessoa com id {id} não encontrada.")

def excluir_pessoa(id):
    pessoa = db_session.query(Pessoas).filter_by(id=id).first()
    if pessoa:
        db_session.delete(pessoa)
        db_session.commit()
        print("Pessoa excluída com sucesso.")
    else:
        print(f"Pessoa com id {id} não encontrada.")

if __name__ == '__main__':
    # Testando as operações
    consulta()
    
