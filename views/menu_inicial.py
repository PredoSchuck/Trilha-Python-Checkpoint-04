from views import JanelaPadrao
from controllers import controlador as contr
from tkinter import messagebox
import customtkinter as ctk

class MenuInicial(JanelaPadrao):
    def __init__(self):
        super().__init__()

        self.frame_lateral = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.frame_lateral.pack(side="left", fill="y")
        
        self.lbl_titulo_menu = ctk.CTkLabel(self.frame_lateral, text="ERP do Futuro", font=self.fonte_titulo)
        self.lbl_titulo_menu.pack(padx=20, pady=20)

        self.frame_central = ctk.CTkFrame(self, corner_radius=10)
        self.frame_central.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.lbl_secao = ctk.CTkLabel(self.frame_central, text="Cadastro de Produtos", font=self.fonte_subtitulo)
        self.lbl_secao.pack(pady=10)

        self.entry_nome = ctk.CTkEntry(self.frame_central, placeholder_text="Nome do Produto", width=300, font=self.fonte_corpo)
        self.entry_nome.pack(pady=8)

        self.entry_preco = ctk.CTkEntry(self.frame_central, placeholder_text="Preço (Ex: 19.90)", width=300, font=self.fonte_corpo)
        self.entry_preco.pack(pady=8)

        self.entry_qtd = ctk.CTkEntry(self.frame_central, placeholder_text="Quantidade em Estoque", width=300, font=self.fonte_corpo)
        self.entry_qtd.pack(pady=8)

        self.btn_gravar = ctk.CTkButton(self.frame_central, text="💾 Gravar Produto", font=self.fonte_corpo, command=self.clique_gravar)
        self.btn_gravar.pack(pady=15)

        self.txt_listagem = ctk.CTkTextbox(self.frame_central, width=500, height=180, font=self.fonte_corpo)
        self.txt_listagem.pack(pady=10)
        self.txt_listagem.configure(state="disabled")

        self.atualizar_visualizacao_lista()

    def clique_gravar(self):
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()
        qtd = self.entry_qtd.get()
        sucesso, mensagem = contr.processar_cadastro(nome, preco, qtd)
        if sucesso:
            messagebox.showinfo("Sucesso!", mensagem)
            self.entry_nome.delete(0, 'end')
            self.entry_preco.delete(0, 'end')
            self.entry_qtd.delete(0, 'end')
            self.atualizar_visualizacao_lista()
        else:
            messagebox.showerror("Erro", mensagem)

    def atualizar_visualizacao_lista(self):
        self.txt_listagem.configure(state="normal")
        self.txt_listagem.delete("1.0", "end")
        produtos = contr.listar_produtos_controlador()
        if not produtos:
            self.txt_listagem.insert("end", "Nenhum produto cadastrado.")
        else:
            for prod in produtos:
                linha = f"ID: {prod[0]} | Produto: {prod[1]} | Preço: R$ {prod[2]:.2f} | Estoque: {prod[3]} un\n"
                self.txt_listagem.insert("end", linha)
        self.txt_listagem.configure(state="disabled")