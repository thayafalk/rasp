import speech_recognition as sr
import pyttsx3
import json

# Configuração do sintetizador de voz para Linux
def falar(texto):
    engine = pyttsx3.init(driverName="espeak")  # Força uso do espeak
    engine.setProperty('voice', 'pt+m3')  # Português masculino
    engine.setProperty('rate', 150)  # Ajusta a velocidade da fala
    engine.say(texto)
    engine.runAndWait()

    engine.stop()  # Libera a engine
    del engine

def carregar_medicamentos():
    try:
        with open("medicamentos_info.json", "r") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def listen():
    recognizer = sr.Recognizer()
    medicamentos = carregar_medicamentos()

    with sr.Microphone() as source:
        falar("Diga o nome do medicamento que deseja saber o uso.")
        print("Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {comando}")

        # Verificar na base de dados de medicamentos
        for medicamento in medicamentos:
            if medicamento["nome"].lower() == comando.lower():
                falar(f"O medicamento {medicamento['nome']} é usado para {medicamento['uso']}.")
                return
        
        falar("Não encontrei esse medicamento na base de dados.")
    except sr.UnknownValueError:
        falar("Não entendi. Tente novamente.")
    except sr.RequestError:
        falar("Erro de conexão com o serviço de reconhecimento.")
