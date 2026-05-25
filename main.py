from controllers.usuario_controller import LoginController

def main():
    print("🚀 Iniciando o sistema...")
    app = LoginController()
    app.iniciar()

if __name__ == "__main__":
    main()