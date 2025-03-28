import pyttsx3

def alertar_emergencia():
    print("Alerta de emergência enviado!")
    engine = pyttsx3.init()
    engine.say("Emergência detectada! Avisando o cuidador.")
    engine.runAndWait()


