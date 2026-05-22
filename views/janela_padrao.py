import os
import customtkinter as ctk

class JanelaPadrao(ctk.CTk):
    def __init__(self, titulo="ERP", largura=900, altura=550):
        super().__init__()

        self.title(titulo)
        self.geometry(f"{largura}x{altura}")
        self.resizable(False, False)

        caminho_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_fonte = os.path.join(caminho_atual, "assets", "Roboto-Regular.ttf")

        self.fonte_titulo = ctk.CTkFont(family="Roboto", size=20, weight="bold")
        self.fonte_subtitulo = ctk.CTkFont(family="Roboto", size=16, weight="bold")
        self.fonte_corpo = ctk.CTkFont(family="Roboto", size=14)
        
        self.cor_principal = "#1f6aa5"
        self.cor_fundo_frames = "#2b2b2b"