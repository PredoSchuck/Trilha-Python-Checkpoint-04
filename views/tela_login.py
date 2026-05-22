import customtkinter as ctk
from tkinter import messagebox
from . import JanelaPadrao
from . import MenuInicial

class TelaLogin(JanelaPadrao):
    def _init_(self):
        super()._init_(titulo="Login - ERP", largura=400, altura=350)

        self.frame_login = ctk.CTkFrame(self, corner_radius=15)
        self.frame_login.pack(pady=40, padx=40, fill="both", expand=True)

        self.lbl_titulo = ctk.CTkLabel(self.frame_login, text="Acesso Restrito", font=self.fonte_titulo)
        self.lbl_titulo.pack(pady=20)

        self.entry_usuario = ctk.CTkEntry(self.frame_login, placeholder_text="Usuário", font=self.fonte_corpo)
        self.entry_usuario.pack(pady=10)

        self.entry_senha = ctk.CTkEntry(self.frame_login, placeholder_text="Senha", show="*", font=self.fonte_corpo)
        self.entry_senha.pack(pady=10)

        self.btn_login = ctk.CTkButton(self.frame_login, text="Entrar", font=self.fonte_corpo, command=self.fazer_login)
        self.btn_login.pack(pady=20)

    def fazer_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario == "admin" and senha == "admin":
            self.destroy()
            app = MenuInicial()
            app.mainloop()
        else:
            messagebox.showerror("Erro de Acesso", "Usuário ou senha incorretos!")