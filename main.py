from models import modelo
# from views import JanelaPadrao
from views import MenuInicial


modelo.criar_tabela()
app = MenuInicial()
app.mainloop()