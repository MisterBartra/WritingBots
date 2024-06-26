# -*- coding: utf-8 -*-
"""Scrapper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zcossy_gWp0hNWrF4tPaybTkDzQ7GIBb
"""
#!pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import BartraUtils

stats = ""

def searchMetadata():
    global value
    driver = webdriver.Edge()
    beatMapIDSize = len(f'{value.split('/')[-1]}')
    
    # Caso solo beatMapID
    if (len(value) == beatMapIDSize):
        value = f"https://osu.ppy.sh/b/{value}"    
    
    # Abre la URL del beatmap
    driver.get(value)
    beatMap = driver.current_url[31::]
    
    trs = driver.find_elements(By.XPATH, "//table[contains(@class,'beatmap-stats-table')]/tbody/tr")

    for index in range(0,len(trs)-1):
        
        trs[index] = trs[index].find_elements(By.TAG_NAME, "td")[1]
        stats = f"{stats}{trs[index].text}"
        if not (index > len(trs)-2):
            stats = f"{stats} | "
    print(stats)
    
    # Extrae los datos necesarios
    
    global mapMetadata
    mapMetadata = [beatMap, stats]
    # Close the browser
    driver.quit()
    #return input("\nPresiona ENTER para comenzar a escribir los datos obtenidos hacia atras en el spreadsheet de la mapPool")


value = ''
mapMetadata=[]

while True:
    value = input("Ingresar URL del mapa ▼\n\t\t  ")
    searchMetadata()   
    BartraUtils.inputRepeater(['DELETE','ENTER'])
    BartraUtils.pyautogui.write(mapMetadata[0])
    BartraUtils.inputRepeater(['ENTER'])
    BartraUtils.inputRepeater(['UP'])
    BartraUtils.inputRepeater(['LEFT'], False, 10)
    BartraUtils.pyautogui.write(mapMetadata[1])
    BartraUtils.inputRepeater(['ENTER'])
    BartraUtils.inputRepeater(['RIGHT'], False, 10)
    
    

