from models import Funcionario, Categoria, Produto, Movimentacao, db_session

def inserir_funcionario():
    funcionario  = Funcionario(nome_funcionario=str(input('Nome: ')),
                     sobrenome=str(input('sobrenome: ')),
                     cpf=str(input('CPF: ')),
                     email=str(input('email: ')),
                     telefone=str(input('telefone: ')),
                     data_de_cadastro=str(input('quando foi cadastrado: '))
                     )
    print(funcionario)
    funcionario.save()

def consulta_funcionario():
    var_funcionario = db_session.query(Funcionario).all()
    print(var_funcionario)

def atualizar_funcionario():
    var_funcionario = db_session.query(Funcionario).filter_by(nome_funcionario=str(input('Nome: ')),
                     cpf=str(input('CPF: '))).first()
    print(var_funcionario)
    var_funcionario.nome_funcionario = str(input('Novo Nome: '))
    var_funcionario.sobrenome = str(input('Novo Sobrenome: '))
    var_funcionario.cpf = str(input('Novo Cpf: '))
    var_funcionario.email = str(input('Novo Email: '))
    var_funcionario.telefone = str(input('Novo Telefone: '))
    var_funcionario.data_de_cadastro = str(input('Novo Data de Cadastro: '))
    db_session.commit()

def deletar_funcionario():
    funcionario = db_session.query(Funcionario).filter_by(nome_funcionario=str(input('Nome: '))).first()
    print(funcionario)
    db_session.delete(funcionario)
    db_session.commit()


def inserir_produto():
    produto = Produto(
        nome_produto=input('Nome do produto: '),
        preco_produto=int(input('Preço do produto: ')),
    )
    print(produto)
    produto.save()

def consulta_produtos():
    produtos = db_session.query(Produto).all()
    for produto in produtos:
        print(produto)

def atualizar_produto():
    id_atual = int(input('ID do produto atual: '))
    var_produto = db_session.query(Produto).filter_by(id_produto=id_atual).first()
    if var_produto:
        print(var_produto)
        novo_nome = input('Novo nome do produto: ')
        novo_preco = int(input('Novo preço do produto: '))
        var_produto.nome_produto = novo_nome
        var_produto.preco_produto = novo_preco
        db_session.commit()
    else:
        print(f"Produto '{id_atual}' not found.")

def deletar_produto():
    id_atual = int(input('ID do produto atual: '))
    produto = db_session.query(Produto).filter_by(id_produto=id_atual).first()
    if produto:
        print(produto)
        db_session.delete(produto)
        db_session.commit()
    else:
        print(f"Produto '{id_atual}' not found.")


def inserir_categoria():
    categoria = Categoria(
        nome_categoria=input('Nome da categoria: ')
    )
    print(categoria)
    categoria.save()

def consulta_categorias():
    categorias = db_session.query(Categoria).all()
    for categoria in categorias:
        print(categoria)

def atualizar_categoria():
    id_atual = int(input('ID da categoria atual: '))
    var_categoria = db_session.query(Categoria).filter_by(id_categoria=id_atual).first()
    if var_categoria:
        print(var_categoria)
        novo_nome = input('Novo nome da categoria: ')
        var_categoria.nome_categoria = novo_nome
        db_session.commit()
    else:
        print(f"Categoria '{id_atual}' not found.")

def deletar_categoria():
    id_atual = int(input('ID da categoria atual: '))
    categoria = db_session.query(Categoria).filter_by(id_categoria=id_atual).first()
    if categoria:
        print(categoria)
        db_session.delete(categoria)
        db_session.commit()
    else:
        print(f"Categoria '{id_atual}' not found.")


def inserir_movimentacao():
    movimentacao = Movimentacao(
        produto_movimentado=input('Produto movimentado: '),
        quantidade_produto=int(input('Quantidade do produto: ')),
        fornecedor=input('Fornecedor: '),
        status=input('Status: '),
        data_da_movimentacao=input('Data da movimentação: '),
    )
    print(movimentacao)
    movimentacao.save()

def consulta_movimentacoes():
    movimentacoes = db_session.query(Movimentacao).all()
    for movimentacao in movimentacoes:
        print(movimentacao)

def atualizar_movimentacao():
    id_atual = int(input('ID da movimentação atual: '))
    var_movimentacao = db_session.query(Movimentacao).filter_by(id_movimentacao=id_atual).first()
    if var_movimentacao:
        print(var_movimentacao)
        novo_produto = input('Novo produto movimentado: ')
        nova_quantidade = int(input('Nova quantidade do produto: '))
        var_movimentacao.produto_movimentado = novo_produto
        var_movimentacao.quantidade_produto = nova_quantidade
        db_session.commit()
    else:
        print(f"Movimentação '{id_atual}' not found.")

if __name__ == '__main__':
    while True:
        escolha = int(input("Menu\n1 - funcionario\n2 - produto\n3 - Categoria\n4 - movimentação\n5 - Sair\nDigite aqui: "))
        if escolha == 1:
            print('"escolha 1"')
            while True:
                escolha1 = int(input("1 - atualizar\n2 - inserir\n3 - consulta\n4 - deletar\n5 - Sair\nDigite aqui: "))
                if escolha1 == 1:
                    atualizar_funcionario()
                elif escolha1 == 2:
                    inserir_funcionario()
                elif escolha1 == 3:
                    consulta_funcionario()
                elif escolha1 == 4:
                    deletar_funcionario()
                elif escolha1 == 5:
                    break
                else:
                    print("escolha invalida")
        elif escolha == 2:
            print('"escolha 2"')
            while True:
                escolha1 = int(input("1 - atualizar\n2 - inserir\n3 - consulta\n4 - deletar\n5 - Sair\nDigite aqui: "))
                if escolha1 == 1:
                    atualizar_produto()
                elif escolha1 == 2:
                    inserir_produto()
                elif escolha1 == 3:
                    consulta_produtos()
                elif escolha1 == 4:
                    deletar_produto()
                elif escolha1 == 5:
                    break
                else:
                    print("escolha invalida")
        elif escolha == 3:
            print('"escolha 3"')
            while True:
                escolha1 = int(input("1 - atualizar\n2 - inserir\n3 - consulta\n4 - deletar\n5 - Sair\nDigite aqui: "))
                if escolha1 == 1:
                    atualizar_categoria()
                elif escolha1 == 2:
                    inserir_categoria()
                elif escolha1 == 3:
                    consulta_categorias()
                elif escolha1 == 4:
                    deletar_categoria()
                elif escolha1 == 5:
                    break
                else:
                    print("escolha invalida")
        elif escolha == 4:
            print('"escolha 4"')
            while True:
                escolha1 = int(input("1 - atualizar\n2 - inserir\n3 - consulta\n4 - Sair\nDigite aqui: "))
                if escolha1 == 1:
                    atualizar_movimentacao()
                elif escolha1 == 2:
                    inserir_movimentacao()
                elif escolha1 == 3:
                    consulta_movimentacoes()
                elif escolha1 == 4:
                    break
                else:
                    print("escolha invalida")

        elif escolha == 5:
            break
        else:
            print('\nopção inválida.\n')



