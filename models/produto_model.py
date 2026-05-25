from . import db_config as db

def inserir_produto(nome, preco, qtd):
    conexao = db.conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", 
        (nome, preco, qtd)
    )
    conexao.commit()
    conexao.close()

def buscar_produtos():
    conexao = db.conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, preco, quantidade FROM produtos")
    dados = cursor.fetchall()
    conexao.close()
    return dados

def atualizar_produto_completo(id_produto, novo_preco, nova_qtd):
    conexao = db.conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE produtos SET preco = ?, quantidade = ? WHERE id = ?", 
        (novo_preco, nova_qtd, id_produto)
    )
    conexao.commit()
    conexao.close()

def deletar_produto(id_produto):
    conexao = db.conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "DELETE FROM produtos WHERE id = ?", 
        (id_produto,)
    )
    conexao.commit()
    conexao.close()

def verificar_produto_existe(nome):
    conexao = db.conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id FROM produtos WHERE LOWER(nome) = LOWER(?)", (nome,))
    produto = cursor.fetchone() 
    
    conexao.close()
    
    return produto is not None