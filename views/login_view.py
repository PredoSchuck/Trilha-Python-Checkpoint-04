import customtkinter as ctk
from tkinter import messagebox
import controllers

class TelaLogin(ctk.CTkToplevel):
    def __init__(self, app_principal):
        super().__init__(master=app_principal)
        
        self.app_principal = app_principal
        
        self.title("Login - ERP")
        self.geometry("400x350")
        
        self.attributes("-topmost", True)
        self.grab_set()

        self.protocol("WM_DELETE_WINDOW", self.fechar_sistema)

        self.frame_login = ctk.CTkFrame(self, corner_radius=15)
        self.frame_login.pack(pady=40, padx=40, fill="both", expand=True)

        self.lbl_titulo = ctk.CTkLabel(self.frame_login, text="Acesso Restrito", font=self.app_principal.fonte_titulo)
        self.lbl_titulo.pack(pady=20)

        self.entry_usuario = ctk.CTkEntry(self.frame_login, placeholder_text="Usuário", font=self.app_principal.fonte_corpo)
        self.entry_usuario.pack(pady=10)

        self.entry_senha = ctk.CTkEntry(self.frame_login, placeholder_text="Senha", show="*", font=self.app_principal.fonte_corpo)
        self.entry_senha.pack(pady=10)

        self.btn_login = ctk.CTkButton(self.frame_login, text="Entrar", font=self.app_principal.fonte_corpo, command=self.fazer_login)
        self.btn_login.pack(pady=20)

    def fazer_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        sucesso, mensagem = controllers.LoginController.processar_login(usuario, senha)

        if sucesso:
            self.destroy()
            self.app_principal.deiconify()
        else:
            messagebox.showerror("Erro de Autenticação", mensagem)
            
    def fechar_sistema(self):
        self.app_principal.destroy()