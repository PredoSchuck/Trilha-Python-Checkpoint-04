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

def criar_tabela_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", ("admin", "admin"))
        
    conexao.commit()
    conexao.close()

def verificar_credenciais(usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
    usuario_encontrado = cursor.fetchone()
    conexao.close()
    return usuario_encontrado is not None

def inserir_usuario(usuario, senha):
    import sqlite3
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
        conexao.commit()
        conexao.close()
        return True, "Usuário cadastrado com sucesso!"
    except sqlite3.IntegrityError:
        conexao.close()
        return False, "Erro: Este nome de usuário já está em uso!"
    
def buscar_dados_dashboard():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, quantidade FROM produtos")
    dados = cursor.fetchall()
    conexao.close()
    return dados