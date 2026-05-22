from models import modelo as mod

def processar_cadastro(nome, p_txt, q_txt):
    if not nome.strip() or not p_txt.strip() or not q_txt.strip():
        return False, "Campos vazios!"

    try:
        preco = float(p_txt.replace(",", "."))
        qtd = int(q_txt)
    except ValueError:
        return False, "Erro nos números!"

    mod.inserir_produto(nome, preco, qtd)
    return True, "Produto cadastrado!"

def listar_produtos_controlador():
    return mod.buscar_produtos()

def processar_atualizacao(id_txt, novo_p_txt):
    if not id_txt.strip() or not novo_p_txt.strip():
        return False, "Campos vazios!"
    
    try:
        id_produto = int(id_txt)
        novo_preco = float(novo_p_txt.replace(",", "."))
    except ValueError:
        return False, "ID ou Preço inválidos!"
        
    mod.atualizar_preco(id_produto, novo_preco)
    return True, "Preço atualizado com sucesso!"

def processar_exclusao(id_txt):
    if not id_txt.strip():
        return False, "Digite o ID do produto!"
        
    try:
        id_produto = int(id_txt)
    except ValueError:
        return False, "ID inválido!"
        
    mod.deletar_produto(id_produto)
    return True, "Produto excluído com sucesso!"

def processar_login(usuario_txt, senha_txt):
    if not usuario_txt.strip() or not senha_txt.strip():
        return False, "Por favor, preencha todos os campos!"
    
    if mod.verificar_credenciais(usuario_txt, senha_txt):
        return True, "Acesso concedido!"
    else:
        return False, "Usuário ou senha incorretos!"
    
def processar_cadastro_usuario(usuario_txt, senha_txt, confirmar_senha_txt):
    """Valida as credenciais e envia para a criação no modelo."""
    if not usuario_txt.strip() or not senha_txt.strip() or not confirmar_senha_txt.strip():
        return False, "Por favor, preencha todos os campos!"
        
    if senha_txt != confirmar_senha_txt:
        return False, "As senhas digitadas não coincidem!"
        
    return mod.inserir_usuario(usuario_txt, senha_txt)

def obter_dados_dashboard():
    return mod.buscar_dados_dashboard()