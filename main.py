from models import modelo
from views import TelaLogin

modelo.criar_tabela()
app = TelaLogin()
app.mainloop()