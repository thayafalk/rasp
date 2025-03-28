import json
import speech_recognition as sr
import pyttsx3
import os

ARQUIVO_MEDICAMENTOS = "medicamentos_controlados.json"

# Inicializa a síntese de voz
engine = pyttsx3.init()

def falar(texto):
    """Converte texto em fala."""
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    """Captura a fala do usuário e retorna o texto reconhecido."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        return recognizer.recognize_google(audio, language="pt-BR").lower()
    except sr.UnknownValueError:
        falar("Não entendi. Tente novamente.")
        return None
    except sr.RequestError:
        falar("Erro na conexão com o serviço de reconhecimento.")
        return None

def adicionar_medicamento_por_voz():
    """Adiciona um medicamento utilizando comandos de voz."""

    falar("Diga o nome do medicamento.")
    nome = None
    while not nome:
        nome = ouvir()

    falar(f"Qual horário para tomar {nome}?")
    horario = None
    while not horario:
        horario = ouvir()

    falar(f"Qual a dosagem de {nome}?")
    dosagem = None
    while not dosagem:
        dosagem = ouvir()

    # Criando a estrutura do medicamento
    novo_medicamento = {
        "nome": nome,
        "horario": horario,
        "dosagem": dosagem
    }

    # Carregar medicamentos existentes
    if os.path.exists(ARQUIVO_MEDICAMENTOS):
        try:
            with open(ARQUIVO_MEDICAMENTOS, "r") as arquivo:
                medicamentos = json.load(arquivo)
        except (json.JSONDecodeError, FileNotFoundError):
            medicamentos = []
    else:
        medicamentos = []

    # Adicionar novo medicamento
    medicamentos.append(novo_medicamento)

    # Salvar no arquivo JSON
    with open(ARQUIVO_MEDICAMENTOS, "w") as arquivo:
        json.dump(medicamentos, arquivo, indent=4)

    falar(f"Medicamento {nome} adicionado com sucesso!")

# Testando a função
if __name__ == "__main__":
    adicionar_medicamento_por_voz()
