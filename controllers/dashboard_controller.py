from models import dashboard_model as mod

class DashboardController:

    @staticmethod
    def obter_dados_dashboard():
        return mod.buscar_dados_dashboard()