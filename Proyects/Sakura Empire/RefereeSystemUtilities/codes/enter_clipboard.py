import pyautogui
import pyperclip
import keyboard
import time

def enviar_oraciones():
    # Espera unos segundos antes de comenzar para que tengas tiempo de colocar el cursor en el campo de chat
    time.sleep(5)

    # Lee el contenido del portapapeles
    clipboard_content = pyperclip.paste()

    # Divide el contenido del portapapeles en oraciones (puedes ajustar la lógica según tus necesidades)
    oraciones = clipboard_content.split('\n')

    # Itera sobre cada oración y envíala en el campo de chat
    for oracion in oraciones:
        # Escribe la oración
        pyautogui.write(oracion)
            
        # Presiona la tecla Enter
        pyautogui.press('enter')

        # Espera un breve momento antes de la siguiente oración (ajusta según sea necesario)
        time.sleep(0.5)

    print("Envío de oraciones completado. Presiona 'R' para ejecutar nuevamente o cualquier otra tecla para salir.")
# Espera a que se presione la tecla 'R' para ejecutar nuevamente
while not keyboard.is_pressed('R'):
    enviar_oraciones()
while  keyboard.is_pressed('R'):
    keyboard.wait('R')

    # Ejecuta la función al inicio
    

