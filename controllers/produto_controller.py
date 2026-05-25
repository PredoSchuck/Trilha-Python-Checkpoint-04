from models import produto_model as mod

class ProdutoController:
    @staticmethod
    def processar_cadastro(nome, p_txt, q_txt):
        if not nome.strip() or not p_txt.strip() or not q_txt.strip():
            return False, "Campos vazios!"
        
        if mod.verificar_produto_existe(nome):
            return False, f"Erro: O produto '{nome}' já está cadastrado no sistema!"
        
        try:
            preco = float(p_txt.replace(",", "."))
            qtd = int(q_txt)
        except ValueError:
            return False, "Erro nos números!"
        
        mod.inserir_produto(nome, preco, qtd)
        return True, "Produto cadastrado!"

    @staticmethod
    def listar_produtos_controlador():
        return mod.buscar_produtos()
    
    @staticmethod
    def processar_atualizacao(id_txt, novo_p_txt, nova_q_txt):
        if not id_txt.strip() or not novo_p_txt.strip() or not nova_q_txt.strip():
            return False, "Campos vazios!"
        
        try:
            id_produto = int(id_txt)
            novo_preco = float(novo_p_txt.replace(",", "."))
            nova_qtd = int(nova_q_txt) 
        except ValueError:
            return False, "ID, Preço ou Quantidade inválidos!"
            
        mod.atualizar_produto_completo(id_produto, novo_preco, nova_qtd)
        return True, "Dados atualizados com sucesso!"
    @staticmethod
    def processar_exclusao(id_txt):
        if not id_txt.strip():
            return False, "Digite o ID do produto!"
            
        try:
            id_produto = int(id_txt)
        except ValueError:
            return False, "ID inválido!"
            
        mod.deletar_produto(id_produto)
        return True, "Produto excluído com sucesso!"