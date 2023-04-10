class BotaoDeEmergencia:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True
        return {"message": "Botão de emergência ligado com sucesso"}

    def desligar(self):
        self.ligado = False
        return {"message": "Botão de emergência desligado com sucesso"}
    
    def get_status(self):
        return { "botao_emergencia": {
                "ligado": self.ligado
            }
        }