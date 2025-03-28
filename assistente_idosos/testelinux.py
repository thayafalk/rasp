import pyttsx3

def falar(texto):
    engine = pyttsx3.init(driverName="espeak")  # Força uso do espeak
    engine.setProperty('rate', 150)  # Ajusta velocidade da fala
    engine.say(texto)
    engine.runAndWait()

falar("Teste de voz no Linux")