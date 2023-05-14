"""Modulo para gerenciamento do botao de emergencia do leito hospitalar."""
class BotaoDeEmergencia:
    """
    Classe para gerenciamento do botao de emergencia do leito hospitalar
    """
    def __init__(self):
        """
        Metodo para inicializar o botao de emergencia como desligado
        """
        self.ligado = False

    def ligar(self):
        """
        Metodo para ligar o botao de emergencia
        """
        self.ligado = True
        return {"message": "Botão de emergência ligado com sucesso"}

    def desligar(self):
        """
        Metodo para desligar o botao de emergencia
        """
        self.ligado = False
        return {"message": "Botão de emergência desligado com sucesso"}

    def get_status(self):
        """
        Metodo para indicar o status do botão de emergencia
        """
        return { "botao_emergencia": {
                "ligado": self.ligado
            }
        }
