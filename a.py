
# Chatbot
import time
import random
import os

def pantalla_carga():
    for i in range(10):
        os.system('cls')
        print('     Procesando mensaje...')
        print('         [' + '#'*i + ']')
        time.sleep(0.5)

def main():
    os.system('cls')
    responses = ['¡Qué interesante!', 'Cuentame más...', 'No sé que decirte... 😔', 'Alejate de mi porfavor', '¿Eres el conocido "Big Six"?']
    print('Bienvenido, empieza a hablar para que el bot responda.')
    input('   > ')
    pantalla_carga()
    print('Respuesta altamente calificada por el bot: \n\t')
    print('>    ' + random.choice(responses))

if __name__ == '__main__':
    main()
class Amigo:
    def __init__(self, calidad: int, carisma: int, inten: int):
        self.calidad = calidad
        self.carisma = carisma
        self.inten = inten
    def saludo(self):
        if self.carisma == 0:
            return "Q'ubo"
        elif self.carisma == 1:
            return "Buenas parcero"
        elif self.carisma == 2:
            return "Buenísima mañana, ¿Cómo está la familia?"
    def apoyo(self):
        if self.calidad == 0:
            return "No, lo lamento bro"
        elif self.calidad == 1:
            return "Bueno, te ayudo. Pero me debes un favor :)"
        elif self.calidad == 2:
            return "De una, cuenta conmigo para lo que necesites"
    def prueba(self):
        if self.inten == 0:
            return "Oye, la verdad siempre me has caído mal. Solo me pasabas tareas."
        elif self.inten == 1:
            return "Siempre te consideré un amigo, confío en tí como tú confías en mí"
        elif self.inten == 2:
            return "Somos mejores amigos :)"
