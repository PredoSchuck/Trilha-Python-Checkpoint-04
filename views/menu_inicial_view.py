from tkinter import messagebox
from .janela_padrao import JanelaPadrao
import controllers 
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MenuInicial(JanelaPadrao):
    def __init__(self):
        super().__init__(titulo="ERP - Sistema de Gestão", largura=1000, altura=600)

        self.frame_lateral = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.frame_lateral.pack(side="left", fill="y")
        
        self.lbl_titulo_menu = ctk.CTkLabel(self.frame_lateral, text="ERP do Futuro", font=self.fonte_titulo)
        self.lbl_titulo_menu.pack(padx=20, pady=20)

        self.btn_nav_cadastro = ctk.CTkButton(
            self.frame_lateral, text="Cadastro de Produto", font=self.fonte_corpo,
            command=lambda: self.mostrar_frame(self.frame_cadastro)
        )
        self.btn_nav_cadastro.pack(pady=10, padx=20, fill="x")

        self.btn_nav_listar = ctk.CTkButton(
            self.frame_lateral, text="Listar Produtos", font=self.fonte_corpo,
            command=lambda: self.mostrar_frame(self.frame_listar)
        )
        self.btn_nav_listar.pack(pady=10, padx=20, fill="x")

        self.btn_nav_atualizar = ctk.CTkButton(
            self.frame_lateral, text="Atualizar Produto", font=self.fonte_corpo,
            command=lambda: self.mostrar_frame(self.frame_atualizar)
        )
        self.btn_nav_atualizar.pack(pady=10, padx=20, fill="x")

        self.btn_nav_excluir = ctk.CTkButton(
            self.frame_lateral, text="Excluir Produto", font=self.fonte_corpo,
            command=lambda: self.mostrar_frame(self.frame_excluir)
        )
        self.btn_nav_excluir.pack(pady=10, padx=20, fill="x")

        self.btn_nav_usuarios = ctk.CTkButton(
            self.frame_lateral, text="Cadastro de Usuários", font=self.fonte_corpo,
            command=lambda: self.mostrar_frame(self.frame_usuarios)
        )
        self.btn_nav_usuarios.pack(pady=10, padx=20, fill="x")

        self.btn_nav_config = ctk.CTkButton(
            self.frame_lateral, text="⚙️ Configurações", font=self.fonte_corpo,
            fg_color="#3d3d3d", hover_color="#575757",
            command=lambda: self.mostrar_frame(self.frame_config)
        )
        self.btn_nav_config.pack(pady=10, padx=20, fill="x")

        self.btn_nav_dash = ctk.CTkButton(
            self.frame_lateral, text="📊 Dashboard", font=self.fonte_corpo,
            fg_color="darkred", hover_color="#aa0000",
            command=lambda: self.mostrar_frame(self.frame_dash)
        )
        self.btn_nav_dash.pack(pady=40, padx=20, fill="x")

        self.frame_cadastro = ctk.CTkFrame(self, corner_radius=10)
        ctk.CTkLabel(self.frame_cadastro, text="Novo Produto", font=self.fonte_subtitulo).pack(pady=20)
        
        self.entry_nome = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Nome do Produto", width=300, font=self.fonte_corpo)
        self.entry_nome.pack(pady=10)
        self.entry_preco = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Preço (Ex: 19.90)", width=300, font=self.fonte_corpo)
        self.entry_preco.pack(pady=10)
        self.entry_qtd = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Quantidade", width=300, font=self.fonte_corpo)
        self.entry_qtd.pack(pady=10)
        
        self.btn_gravar = ctk.CTkButton(self.frame_cadastro, text="Gravar Produto", font=self.fonte_corpo, command=self.clique_gravar)
        self.btn_gravar.pack(pady=20)

        self.frame_listar = ctk.CTkFrame(self, corner_radius=10)
        ctk.CTkLabel(self.frame_listar, text="Estoque Atual", font=self.fonte_subtitulo).pack(pady=20)
        
        self.entry_pesquisa = ctk.CTkEntry(self.frame_listar, placeholder_text="Pesquisar por nome...", width=400, font=self.fonte_corpo)
        self.entry_pesquisa.pack(pady=10)
        
        self.txt_listagem = ctk.CTkTextbox(self.frame_listar, width=600, height=300, font=self.fonte_corpo)
        self.txt_listagem.pack(pady=10)

        self.frame_atualizar = ctk.CTkFrame(self, corner_radius=10)
        ctk.CTkLabel(self.frame_atualizar, text="Atualizar Preço", font=self.fonte_subtitulo).pack(pady=20)
        
        self.entry_id_att = ctk.CTkEntry(self.frame_atualizar, placeholder_text="ID do Produto", width=300, font=self.fonte_corpo)
        self.entry_id_att.pack(pady=10)

        self.entry_preco_novo = ctk.CTkEntry(self.frame_atualizar, placeholder_text="Novo Preço", width=300, font=self.fonte_corpo)
        self.entry_preco_novo.pack(pady=10)
        
        self.entry_qtd_nova = ctk.CTkEntry(self.frame_atualizar, placeholder_text="Nova Quantidade", width=300, font=self.fonte_corpo)
        self.entry_qtd_nova.pack(pady=10)
        
        self.btn_att = ctk.CTkButton(self.frame_atualizar, text="Atualizar Dados", font=self.fonte_corpo, command=self.clique_atualizar)
        self.btn_att.pack(pady=20)

        self.frame_excluir = ctk.CTkFrame(self, corner_radius=10)
        ctk.CTkLabel(self.frame_excluir, text="Deletar Produto", font=self.fonte_subtitulo).pack(pady=20)
        
        self.entry_id_del = ctk.CTkEntry(self.frame_excluir, placeholder_text="ID do Produto para Excluir", width=300, font=self.fonte_corpo)
        self.entry_id_del.pack(pady=10)
        
        self.btn_del = ctk.CTkButton(self.frame_excluir, text="Excluir", font=self.fonte_corpo, fg_color="red", hover_color="darkred", command=self.clique_excluir)
        self.btn_del.pack(pady=20)

        self.frame_config = ctk.CTkFrame(self, corner_radius=10)
        ctk.CTkLabel(self.frame_config, text="Configurações do Sistema", font=self.fonte_subtitulo).pack(pady=20)
        
        ctk.CTkLabel(self.frame_config, text="Tema Visual do Aplicativo:", font=self.fonte_corpo).pack(pady=5)
        self.switch_tema = ctk.CTkSwitch(self.frame_config, text="Modo Claro", font=self.fonte_corpo, command=self.alternar_tema)
        self.switch_tema.pack(pady=10)

        self.frame_usuarios = ctk.CTkFrame(self, corner_radius=10)
        ctk.CTkLabel(self.frame_usuarios, text="Registrar Novo Usuário", font=self.fonte_subtitulo).pack(pady=20)
        
        self.entry_novo_user = ctk.CTkEntry(self.frame_usuarios, placeholder_text="Nome de Usuário", width=300, font=self.fonte_corpo)
        self.entry_novo_user.pack(pady=10)
        
        self.entry_nova_senha = ctk.CTkEntry(self.frame_usuarios, placeholder_text="Senha", show="*", width=300, font=self.fonte_corpo)
        self.entry_nova_senha.pack(pady=10)
        
        self.entry_confirmar_senha = ctk.CTkEntry(self.frame_usuarios, placeholder_text="Confirmar Senha", show="*", width=300, font=self.fonte_corpo)
        self.entry_confirmar_senha.pack(pady=10)
        
        self.btn_salvar_user = ctk.CTkButton(self.frame_usuarios, text="👤 Salvar Usuário", font=self.fonte_corpo, command=self.clique_gravar_usuario)
        self.btn_salvar_user.pack(pady=20)

        self.frame_dash = ctk.CTkFrame(self, corner_radius=10)
        ctk.CTkLabel(self.frame_dash, text="Dashboard Analítico", font=self.fonte_subtitulo).pack(pady=20)

        self.frames = [
            self.frame_cadastro, self.frame_listar, self.frame_atualizar, 
            self.frame_excluir, self.frame_usuarios, self.frame_config, self.frame_dash
        ]
        
        self.mostrar_frame(self.frame_cadastro)

    def alternar_tema(self):
        if self.switch_tema.get() == 1:
            ctk.set_appearance_mode("Light")
            self.switch_tema.configure(text="Modo Escuro")
        else:
            ctk.set_appearance_mode("Dark")
            self.switch_tema.configure(text="Modo Claro")

    def clique_gravar(self):
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()
        qtd = self.entry_qtd.get()
        
        sucesso, mensagem = controllers.ProdutoController.processar_cadastro(nome, preco, qtd)
        if sucesso:
            messagebox.showinfo("Sucesso!", mensagem)
            self.entry_nome.delete(0, 'end')
            self.entry_preco.delete(0, 'end')
            self.entry_qtd.delete(0, 'end')
        else:
            messagebox.showerror("Erro de Validação", mensagem)

    def atualizar_visualizacao_lista(self):
        self.txt_listagem.configure(state="normal")
        self.txt_listagem.delete("1.0", "end")
        
        produtos = controllers.ProdutoController.listar_produtos_controlador()
        if not produtos:
            self.txt_listagem.insert("end", "Nenhum produto cadastrado no momento.")
        else:
            for prod in produtos:
                linha = f"ID: {prod[0]} | Produto: {prod[1]} | Preço: R$ {prod[2]:.2f} | Estoque: {prod[3]} un\n"
                self.txt_listagem.insert("end", linha)
                
        self.txt_listagem.configure(state="disabled")

    def clique_atualizar(self):
        id_txt = self.entry_id_att.get()
        preco_txt = self.entry_preco_novo.get()
        qtd_txt = self.entry_qtd_nova.get()

        sucesso, msg = controllers.ProdutoController.processar_atualizacao(id_txt, preco_txt, qtd_txt)
        
        if sucesso:
            messagebox.showinfo("Sucesso", msg)
            self.entry_id_att.delete(0, 'end')
            self.entry_preco_novo.delete(0, 'end')
            self.entry_qtd_nova.delete(0, 'end')
        else:
            messagebox.showerror("Erro", msg)

    def clique_excluir(self):
        id_txt = self.entry_id_del.get()
        
        sucesso, msg = controllers.ProdutoController.processar_exclusao(id_txt)
        if sucesso:
            messagebox.showinfo("Sucesso", msg)
            self.entry_id_del.delete(0, 'end')
        else:
            messagebox.showerror("Erro", msg)

    def clique_gravar_usuario(self):
        usuario = self.entry_novo_user.get()
        senha = self.entry_nova_senha.get()
        confirmacao = self.entry_confirmar_senha.get()
        
        sucesso, mensagem = controllers.LoginController.processar_cadastro_usuario(usuario, senha, confirmacao)
        if sucesso:
            messagebox.showinfo("Sucesso!", mensagem)
            self.entry_novo_user.delete(0, 'end')
            self.entry_nova_senha.delete(0, 'end')
            self.entry_confirmar_senha.delete(0, 'end')
        else:
            messagebox.showerror("Erro", mensagem)

        
    def desenhar_grafico(self):
        for widget in self.frame_dash.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "Dashboard Analítico":
                continue
            widget.destroy()

        dados = controllers.DashboardController.obter_dados_dashboard()

        if not dados:
            ctk.CTkLabel(self.frame_dash, text="Sem dados suficientes para gerar o gráfico.", font=self.fonte_corpo).pack(pady=50)
            return

        nomes = [item[0] for item in dados]
        quantidades = [item[1] for item in dados]

        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        
        ax.pie(quantidades, labels=nomes, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        ax.set_title("Proporção de Stock por Produto")

        canvas = FigureCanvasTkAgg(fig, master=self.frame_dash)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20, fill="both", expand=True)

    def mostrar_frame(self, frame_desejado):
        for frame in self.frames:
            frame.pack_forget()
            
        frame_desejado.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        
        if frame_desejado == self.frame_listar:
            self.atualizar_visualizacao_lista()
        elif frame_desejado == self.frame_dash:
            self.desenhar_grafico()