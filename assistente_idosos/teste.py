import speech_recognition as sr
import pyttsx3

# Função para falar
def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Função para ouvir os comandos
def ouvir_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ajustando para o ruído ambiente...")
        recognizer.adjust_for_ambient_noise(source)
        print("Diga algo!")
        audio = recognizer.listen(source)
    
    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        falar("Não entendi. Tente novamente.")
        return None
    except sr.RequestError:
        print("Erro de conexão com o serviço de reconhecimento.")
        falar("Erro de conexão com o serviço de reconhecimento.")
        return None

# Exemplo de uso
if __name__ == "__main__":
    while True:
        comando = ouvir_comando()
        if comando == "sair":
            falar("Saindo do assistente.")
            break
