import os
import customtkinter as ctk

ctk.set_appearance_mode("Dark")

class JanelaPadrao(ctk.CTk):
    def __init__(self, titulo="ERP", largura=900, altura=550):
        super().__init__()

        self.title(titulo)
        self.geometry(f"{largura}x{altura}")
        self.resizable(False, False)

        caminho_views = os.path.dirname(os.path.abspath(__file__))
        caminho_raiz = os.path.dirname(caminho_views)
        caminho_fonte = os.path.join(caminho_raiz, "assets", "Roboto-Regular.ttf")

        if os.path.exists(caminho_fonte):
            ctk.FontManager.load_font(caminho_fonte)
            familia_fonte = "Roboto"
        else:
            print(f"⚠️ Aviso: Fonte não encontrada em {caminho_fonte}. Usando fonte padrão.")
            familia_fonte = "Arial" 

        self.fonte_titulo = ctk.CTkFont(family=familia_fonte, size=20, weight="bold")
        self.fonte_subtitulo = ctk.CTkFont(family=familia_fonte, size=16, weight="bold")
        self.fonte_corpo = ctk.CTkFont(family=familia_fonte, size=14)
        
        self.cor_principal = "#1f6aa5"
        self.cor_fundo_frames = "#2b2b2b"