import speech_recognition as sr
import pyttsx3
import json

# Função para falar
def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Função para carregar os dados de medicamentos do arquivo JSON
def carregar_medicamentos():
    try:
        with open("medicamentos_info.json", "r") as arquivo:
            medicamentos = json.load(arquivo)
        return medicamentos
    except FileNotFoundError:
        print("Arquivo de medicamentos não encontrado.")
        return {}
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON.")
        return {}

# Função para falar sobre o medicamento
def falar_info_medicamento(medicamento, medicamentos_info):
    if medicamento in medicamentos_info:
        falar(medicamentos_info[medicamento])
    else:
        falar("Medicamento não encontrado na base de dados.")

# Função para ouvir comandos de voz
def ouvir_comandos():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        falar("Estou ouvindo. Diga o nome de um medicamento.")
        print("Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", comando)
        
        # Carregar dados dos medicamentos do arquivo
        medicamentos_info = carregar_medicamentos()
        
        if medicamentos_info:
            # Chama a função para falar sobre o medicamento
            falar_info_medicamento(comando, medicamentos_info)
        else:
            falar("Não foi possível carregar os dados dos medicamentos.")
    
    except sr.UnknownValueError:
        falar("Não entendi. Tente novamente.")
    except sr.RequestError:
        falar("Erro de conexão com o serviço de reconhecimento.")