from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import scoped_session,sessionmaker,relationship
from sqlalchemy.orm import declarative_base


#criando banco de dados
engine = create_engine('sqlite:///atividade.db')

db_session = scoped_session(sessionmaker(autocommit = False,bind= engine))

Base = declarative_base()
Base.query = db_session.query_property()

#criando a tabela 

class Pessoas(Base):
    __tablename__='pessoas'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(30), nullable=False)
    sobrenome = Column(String(30), nullable=False)
    idade = Column(Integer, nullable=False)
    
    def __repr__(self):
        return (
            f"\nid={self.id},\nnome ='{self.nome}',\nsobrenome ='{self.sobrenome}',\nidade ={self.idade}\n"
        )
    
    def save(self):
        db_session.add(self)
        db_session.commit()
        
    def delete(self):
        db_session.delete(self)
        db_session.commit()   
    
    
class Atividade(Base):
    __tablename__ = 'atividade'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nomeAtividade = Column(String(30), nullable=False, index=True)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'), nullable=False)
    
    pessoas = relationship("Pessoas")
    
    def __repr__(self):
        return (
            f"Atividade\nid={self.id}, \natividade='{self.nomeAtividade}', \npessoa_id={self.pessoa_id})>"
        )
    
    def save(self):
        db_session.add(self)
        db_session.commit()
        
    def delete(self):
        db_session.delete(self)
        db_session.commit()
    
def init_db():
    Base.metadata.create_all(bind=engine)
    
if __name__ == '__main__':
    init_db()
    
    
    