from models import modelo

def processar_cadastro(nome, p_txt, q_txt):
    if not nome.strip() or not p_txt.strip() or not q_txt.strip():
        return False, "Campos vazios!"

    try:
        preco = float(p_txt.replace(",", "."))
        qtd = int(q_txt)
    except ValueError:
        return False, "Erro nos números!"

    modelo.inserir_produto(nome, preco, qtd)
    return True, "Produto cadastrado!"

def listar_produtos_controlador():
    return modelo.buscar_produtos()

def processar_atualizacao(id_txt, novo_p_txt):
    if not id_txt.strip() or not novo_p_txt.strip():
        return False, "Campos vazios!"
    
    try:
        id_produto = int(id_txt)
        novo_preco = float(novo_p_txt.replace(",", "."))
    except ValueError:
        return False, "ID ou Preço inválidos!"
        
    modelo.atualizar_preco(id_produto, novo_preco)
    return True, "Preço atualizado com sucesso!"

def processar_exclusao(id_txt):
    if not id_txt.strip():
        return False, "Digite o ID do produto!"
        
    try:
        id_produto = int(id_txt)
    except ValueError:
        return False, "ID inválido!"
        
    modelo.deletar_produto(id_produto)
    return True, "Produto excluído com sucesso!"