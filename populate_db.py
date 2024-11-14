import random
from datetime import datetime, timedelta
from faker import Faker
from models import db_session, Funcionario, Produto, Categoria, Movimentacao, init_db

# Configuração para dados em português
fake = Faker('pt_BR')

def create_fake_funcionarios(num):
    for _ in range(num):
        funcionario = Funcionario(
            nome_funcionario=fake.first_name(),
            sobrenome=fake.last_name(),
            email=fake.unique.email(),
            cpf=fake.unique.random_int(min=10000000000, max=99999999999),
            telefone=fake.phone_number(),
            data_de_cadastro=fake.date_this_decade().isoformat()
        )
        funcionario.save()

def create_fake_categorias(num):
    categorias = [
        'Eletrônicos', 'Alimentos', 'Roupas', 'Móveis', 'Livros',
        'Ferramentas', 'Brinquedos', 'Cosméticos', 'Esporte',
        'Jardinagem', 'Veículos', 'Informática', 'Bebidas',
        'Utensílios Domésticos', 'Material Escolar'
    ]
    for i in range(num):
        categoria = Categoria(
            nome_categoria=categorias[i % len(categorias)]  # Cicla pelas categorias realistas
        )
        categoria.save()

def create_fake_produtos(num, categoria_ids):
    produtos = [
        'Smartphone', 'Notebook', 'Geladeira', 'Televisão', 'Bicicleta',
        'Sofá', 'Livro', 'Cafeteira', 'Fogão', 'Fone de Ouvido',
        'Mouse', 'Teclado', 'Cerveja', 'Refrigerante', 'Camiseta',
        'Chave Inglesa', 'Boneca', 'Brinquedo de Montar', 'Shampoo',
        'Bola de Futebol', 'Tesoura', 'Regador', 'Carro', 'Motocicleta'
    ]
    for _ in range(num):
        produto = Produto(
            nome_produto=random.choice(produtos),
            preco_produto=round(random.uniform(10.0, 2000.0), 2),
            id_categoria=random.choice(categoria_ids)
        )
        produto.save()

def create_fake_movimentacoes(num, funcionario_ids, produto_ids):
    for _ in range(num):
        movimentacao = Movimentacao(
            produto_movimentado=fake.word(ext_word_list=['Entrada', 'Saída']),
            quantidade_produto=random.randint(1, 100),
            fornecedor=fake.company(),
            status=random.choice(['Entrada', 'Saída']),
            data_da_movimentacao=fake.date_this_decade(),
            id_funcionario=random.choice(funcionario_ids),
            id_produto=random.choice(produto_ids)
        )
        movimentacao.save()

def main():
    init_db()

    # Criando dados fictícios
    create_fake_funcionarios(50)
    funcionarios = db_session.query(Funcionario).all()
    funcionario_ids = [f.id_funcionario for f in funcionarios]

    create_fake_categorias(10)
    categorias = db_session.query(Categoria).all()
    categoria_ids = [c.id_categoria for c in categorias]

    create_fake_produtos(100, categoria_ids)
    produtos = db_session.query(Produto).all()
    produto_ids = [p.id_produto for p in produtos]

    create_fake_movimentacoes(200, funcionario_ids, produto_ids)

    print("Banco de dados populado com dados fictícios.")

if __name__ == '__main__':
    main()
