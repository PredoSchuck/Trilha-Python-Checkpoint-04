from models import usuario_model as mod
from views import TelaLogin
from views import MenuInicial

class LoginController:
    def __init__(self):
        pass
    
    def iniciar(self):
        from models import criar_tabela_produtos, criar_tabela_usuarios
        
        print("🔨 Inicializando banco de dados...")
        criar_tabela_produtos()
        criar_tabela_usuarios()

        app = MenuInicial()
        app.withdraw() 
        tela_login = TelaLogin(app_principal=app)
        app.mainloop()

    @staticmethod
    def processar_login(usuario_txt, senha_txt):
        if not usuario_txt.strip() or not senha_txt.strip():
            return False, "Por favor, preencha todos os campos!"
        
        if mod.verificar_credenciais(usuario_txt, senha_txt):
            return True, "Acesso concedido!"
        else:
            return False, "Usuário ou senha incorretos!"
        
    @staticmethod
    def processar_cadastro_usuario(usuario_txt, senha_txt, confirmar_senha_txt):
        if not usuario_txt.strip() or not senha_txt.strip() or not confirmar_senha_txt.strip():
            return False, "Por favor, preencha todos os campos!"
            
        if senha_txt != confirmar_senha_txt:
            return False, "As senhas digitadas não coincidem!"
            
        return mod.inserir_usuario(usuario_txt, senha_txt)