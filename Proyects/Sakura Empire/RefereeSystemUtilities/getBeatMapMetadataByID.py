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

beatMapID = '0'
stars = '0.0'
musicData = ' '
mapSetID = '0'

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
    
    # Caso link extendido
    #if (len(value) > 31 + len(beatMap)):
    beatMapID = beatMap.split('/')[-1]  # ID de la Dificultad
    mapSetID = beatMap[0:len(beatMap)-len(f'#osu/{beatMapID}')]  # ID del Paquete de Mapas

    # Extrae los datos necesarios
    songMetadata = f"{driver.find_elements(By.CLASS_NAME, 'beatmapset-header__details-text-link')[1].text} - {driver.find_element(By.CLASS_NAME, 'beatmapset-header__details-text-link').text}"
    stars = f"{driver.find_elements(By.CLASS_NAME, 'beatmap-stats-table__value')[4].text.split(',')[0]}.{driver.find_elements(By.CLASS_NAME, 'beatmap-stats-table__value')[4].text.split(',')[-1]} \u2605"
    
    global mapMetadata
    mapMetadata = [f"=IMAGE(\"https://assets.ppy.sh/beatmaps/{mapSetID}/covers/cover.jpg\")", songMetadata, stars, beatMapID]
    mapMetadata.reverse()
    print(f"\nAsigna hacia atrás siguiendo este orden:\n  {mapMetadata} ")
    # Close the browser
    driver.quit()
    #return input("\nPresiona ENTER para comenzar a escribir los datos obtenidos hacia atras en el spreadsheet de la mapPool")


value = ''
mapMetadata=[]

while True:
    value = input("Ingresar URL del mapa ▼\n\t\t  ")
    if (len(value) < 2):
        continue
    searchMetadata()
    for indexData in mapMetadata:
        BartraUtils.inputRepeater(['DELETE','ENTER'])
        BartraUtils.pyautogui.write(indexData)
        BartraUtils.inputRepeater('ENTER')
        BartraUtils.inputRepeater(['LEFT','UP'])
    BartraUtils.inputRepeater(['DOWN'], False, 2)
    BartraUtils.inputRepeater(['RIGHT'], False, 4)