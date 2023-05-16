from fastapi import FastAPI, Request
from botao_emergencia import BotaoDeEmergencia

app = FastAPI()
botao_emergencia = BotaoDeEmergencia()

@app.get("/")
def read_root():
    return {"message": "botao_emergencia"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/status")
def check_status():
    return botao_emergencia.get_status()

@app.put("/ligar")
def ligar():
    return botao_emergencia.ligar()

@app.put("/desligar")
def desligar():
    botao_emergencia.desligar()
    return {"message": "botao_emergencia desligado"}