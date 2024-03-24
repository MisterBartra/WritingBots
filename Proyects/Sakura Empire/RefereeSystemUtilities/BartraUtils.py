import pyautogui
import time

def inputRepeater(inputKey=[], hotkeys=False, repeat=1):
    for key in range(repeat):
        time.sleep(0.1)
        if (not hotkeys):
            pyautogui.press(inputKey)
            time.sleep(0.05)
        else:
            pyautogui.hotkey(inputKey)

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds=seconds-1
