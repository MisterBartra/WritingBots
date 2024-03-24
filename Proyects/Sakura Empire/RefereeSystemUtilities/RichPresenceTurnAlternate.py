import BartraUtils

bronya = [
    "https://www.youtube.com/embed/xTK8P6vRiIg?t=5&autoplay=true",
    "https://www.youtube.com/embed/uxG8ZgJdxso?t=5&autoplay=true",
    "https://www.youtube.com/embed/WWUp8OS4zmc?t=5&autoplay=true"
    ]
seele = [
    "https://www.youtube.com/embed/N-VNG8vW5RA?t=5&autoplay=true",
    "https://www.youtube.com/embed/Yalse6jPbbE?t=5&autoplay=true",
    "https://www.youtube.com/embed/ghd9qiBHBcU?t=5&autoplay=true"
]

def terceroInvertir(text, indexPP=0):
    if (text=="[ Bronya ]"):
        if(indexPP==1):
            return f"Symphony of {text[2:8]}"
        if(indexPP==2):
            return "Seele+ "
    elif (text=="[ Seele ]"):
        if(indexPP==1):
            return f"Symphony of {text[2:7]}"
        if(indexPP==2):
            return "Bronya+ "
    return text

BartraUtils.countdown(10)

# Inicializar un índice para recorrer el arreglo
indice = 0
direccion = -1
BartraUtils.inputRepeater(['tab','tab','tab','tab','tab','tab','tab','tab','tab','tab','tab'])

# Mientras el índice esté dentro de los límites del arreglo
while 0 <= indice < len(bronya):
    BartraUtils.pyautogui.write(terceroInvertir("[ Bronya ]", indice))
    BartraUtils.inputRepeater('tab')
    BartraUtils.pyautogui.write(bronya[indice])
    BartraUtils.inputRepeater('tab')
    BartraUtils.pyautogui.write(terceroInvertir("[ Seele ]", indice))
    BartraUtils.inputRepeater('tab')
    BartraUtils.pyautogui.write(seele[indice])
    BartraUtils.inputRepeater('tab', 'enter')
    BartraUtils.inputRepeater(['shift', 'tab'], True, 4)
    
    # Cambiar la dirección del recorrido
    if (indice == 0 or indice == len(bronya)-1):
        direccion *= -1
    # Actualizar el índice según la dirección
        indice += direccion 
    input("Presione ENTER para continuar")
    #BartraUtils.time.sleep(600)
    BartraUtils.countdown(10)
