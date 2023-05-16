"""
Modulo para inicialização e disponilibilização do serviço
relacionado à bomba de infusão de medicamentos.
"""
from fastapi import FastAPI
from botao_emergencia import BotaoDeEmergencia

app = FastAPI()
botao_emergencia = BotaoDeEmergencia()

@app.get("/")
def read_root():
    """Metodo para roteamento inicial do componente"""
    return {"message": "botao_emergencia"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/status")
def check_status():
    """Metodo para roteamento para checagem de status do botao de emergencia"""
    return botao_emergencia.get_status()

@app.put("/ligar")
def ligar():
    """Metodo para roteamento para ligar o botão de emergencia"""
    return botao_emergencia.ligar()

@app.put("/desligar")
def desligar():
    """Metodo para roteamento para desligar o botão de emergencia"""
    botao_emergencia.desligar()
    return {"message": "botao_emergencia desligado"}
