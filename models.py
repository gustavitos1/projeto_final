from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, declarative_base

engine = create_engine('sqlite:///sql_prejetofinal.db')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id_funcionario = Column(Integer, primary_key=True)
    nome_funcionario = Column(String(40), nullable=False, index=True)
    sobrenome = Column(String(16), nullable=False, index=True)
    email = Column(String(40), nullable=False, index=True, unique=True)
    cpf = Column(String(11), nullable=False, index=True, unique=True)
    telefone = Column(String(16), index=True, unique=True)
    data_de_cadastro = Column(String, index=True)

    def __repr__(self):
        return '<Funcionario: {} {}>'.format(self.nome_funcionario, self.sobrenome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_funcionario(self):
        dados_funcionario = {
            "id_funcionario": self.id_funcionario,
            "nome_funcionario": self.nome_funcionario,
            "sobrenome": self.sobrenome,
            "email": self.email,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "data_de_cadastro": self.data_de_cadastro
        }
        return dados_funcionario

class Produto(Base):
    __tablename__ = 'produtos'
    id_produto = Column(Integer, primary_key=True)
    nome_produto = Column(String(40), nullable=False, index=True)
    preco_produto = Column(Float, index=True)
    id_categoria = Column(Integer, ForeignKey('categorias.id_categoria'))
    categoria = relationship("Categoria")

    def __repr__(self):
        return '<Produto: {}>'.format(self.nome_produto)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_produto(self):
        dados_produto = {
            "id_produto": self.id_produto,
            "nome_produto": self.nome_produto,
            "preco_produto": self.preco_produto
        }
        return dados_produto

class Categoria(Base):
    __tablename__ = 'categorias'
    id_categoria = Column(Integer, primary_key=True)
    nome_categoria = Column(String(40), nullable=False, index=True)

    def __repr__(self):
        return '<Categoria: {}>'.format(self.nome_categoria)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_categoria(self):
        dados_categoria = {
            "id_categoria": self.id_categoria,
            "nome_categoria": self.nome_categoria
        }
        return dados_categoria

class Movimentacao(Base):
    __tablename__ = 'movimentacoes'
    id_movimentacao = Column(Integer, primary_key=True)
    produto_movimentado = Column(String(40), nullable=False, index=True)
    quantidade_produto = Column(Integer, index=True)
    fornecedor = Column(String(11), index=True)
    status = Column(String(11), index=True)
    data_da_movimentacao = Column(Date, index=True)
    id_funcionario = Column(Integer, ForeignKey('funcionarios.id_funcionario'))
    funcionario = relationship("Funcionario")
    id_produto = Column(Integer, ForeignKey('produtos.id_produto'))
    Produto = relationship("Produto")

    def __repr__(self):
        return '<Movimentacao: {}>'.format(self.produto_movimentado)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_movimentacao(self):
        dados_movimentacao = {
            "id_movimentacao": self.id_movimentacao,
            "produto_movimentado": self.produto_movimentado,
            "quantidade_produto": self.quantidade_produto,
            "fornecedor": self.fornecedor,
            "status": self.status,
            "data_da_movimentacao": self.data_da_movimentacao
        }
        return dados_movimentacao

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()