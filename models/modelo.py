import sqlite3

def conectar():
    return sqlite3.connect("inventario.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def inserir_produto(nome, preco, qtd):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", 
        (nome, preco, qtd)
    )
    conexao.commit()
    conexao.close()

def buscar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, preco, quantidade FROM produtos")
    dados = cursor.fetchall()
    conexao.close()
    return dados

def atualizar_preco(id_produto, novo_p):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE produtos SET preco = ? WHERE id = ?", 
        (novo_p, id_produto)
    )
    conexao.commit()
    conexao.close()

def deletar_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "DELETE FROM produtos WHERE id = ?", 
        (id_produto,)
    )
    conexao.commit()
    conexao.close()

criar_tabela()