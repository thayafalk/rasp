import time

def verificar_lembretes():
    while True:
        hora_atual = time.strftime("%H:%M")
        print(f"Verificando lembretes às {hora_atual}")
        time.sleep(60)


''' emergency_alert.py - Módulo para chamadas de emergência '''
def alertar_emergencia():
    print("Alerta de emergência enviado!")
    print("Emergência detectada! Avisando o cuidador.")
