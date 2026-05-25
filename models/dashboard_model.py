from . import db_config as db

def buscar_dados_dashboard():
    conexao = db.conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, quantidade FROM produtos")
    dados = cursor.fetchall()
    conexao.close()
    return dados