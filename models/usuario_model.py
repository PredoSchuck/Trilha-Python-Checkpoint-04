from . import db_config as db

def verificar_credenciais(usuario, senha):
    conexao = db.conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
    usuario_encontrado = cursor.fetchone()
    conexao.close()
    return usuario_encontrado is not None

def inserir_usuario(usuario, senha):
    import sqlite3
    conexao = db.conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
        conexao.commit()
        conexao.close()
        return True, "Usuário cadastrado com sucesso!"
    except sqlite3.IntegrityError:
        conexao.close()
        return False, "Erro: Este nome de usuário já está em uso!"