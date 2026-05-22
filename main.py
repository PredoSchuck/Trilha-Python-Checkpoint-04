from models import modelo
from views import MenuInicial
from views import TelaLogin

def main():
    print("🔨 Inicializando banco de dados...")
    modelo.criar_tabela()
    modelo.criar_tabela_usuarios()

    print("🚀 Iniciando o sistema...")

    app = MenuInicial()
    app.withdraw() 
    tela_login = TelaLogin(app_principal=app)
    app.mainloop()

main()