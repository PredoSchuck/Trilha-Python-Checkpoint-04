from .db_config import conectar, criar_tabela_produtos, criar_tabela_usuarios
from .produto_model import inserir_produto, buscar_produtos, atualizar_produto_completo, deletar_produto, verificar_produto_existe
from .usuario_model import verificar_credenciais, inserir_usuario
from .dashboard_model import buscar_dados_dashboard