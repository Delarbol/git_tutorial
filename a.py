
# Chatbot
import time
import random
import os

def pantalla_carga():
    for i in range(10):
        if os.name == 'nt':
            _ = os.system('cls')
        print('     Procesando mensaje...')
        print('         [' + '#'*i + ']')
        time.sleep(0.5)

def main():
    responses = ['¡Qué interesante!', 'Cuentame más...', 'No sé que decirte... 😔', 'Alejate de mi porfavor', '¿Eres el conocido "Big Six"?']
    print('Bienvenido, empieza a hablar para que el bot responda.')
    input('   > ')
    pantalla_carga()
    print('Respuesta altamente calificada por el bot: \n\t')
    print('>    ' + random.choice(responses))

if __name__ == '__main__':
    main()
