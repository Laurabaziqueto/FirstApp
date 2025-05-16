from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, relationship

# PrimaryKeyConstraint significa um valores unicos e na nulos, exclusivo de cada registro na tabela
engine = create_engine('sqlite:///techstock.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id_funcionario = Column(Integer, primary_key=True)
    nome = Column(String(255))
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(150), unique=True)
    telefone = Column(Integer, unique=True, nullable=False)
    status_funcionario = Column(String(255))
    cpf = Column(String(255), unique=True, nullable=False)
    data_registro = Column(String(255))

    def __repr__(self):
        return '<funcionario: {} {} {} {}>'.format(self.nome, self.email, self.telefone, self.cpf)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_funcionario(self):
        dados_funcionario = {
            "id_funcionario": self.id_funcionario,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "telefone": self.telefone,
            "status": self.status_funcionario,
            "cpf": self.cpf,
            "data_registro": self.data_registro,
        }
        return dados_funcionario


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()