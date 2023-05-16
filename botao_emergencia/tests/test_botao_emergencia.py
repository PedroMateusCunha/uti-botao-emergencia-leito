import pytest
import sys
import os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)
from botao_emergencia import *

@pytest.fixture
def botao_emergencia():
    return BotaoDeEmergencia()

def test_inicializacao(botao_emergencia):
    assert not botao_emergencia.ligado

def test_ligar(botao_emergencia):
    resultado = botao_emergencia.ligar()
    assert resultado == {"message": "Botão de emergência ligado com sucesso"}
    assert botao_emergencia.ligado

def test_desligar(botao_emergencia):
    botao_emergencia.ligar()  # Ligar o botão antes de desligar
    resultado = botao_emergencia.desligar()
    assert resultado == {"message": "Botão de emergência desligado com sucesso"}
    assert not botao_emergencia.ligado

def test_get_status(botao_emergencia):
    resultado = botao_emergencia.get_status()
    assert resultado == {"botao_emergencia": {"ligado": botao_emergencia.ligado}}