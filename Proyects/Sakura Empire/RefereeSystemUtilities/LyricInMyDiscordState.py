"""Scrapper.ipynb
"""
#!pip install selenium
# id=  account-set-custom-status
# avatarWrapper_ba5175 withTagAsButton_cc125f

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import BartraUtils

mode='#osu/'

beatMapID = '0'
stars = '0.0'
musicData = ' '
mapSetID = '0'

avatarWrapper='withTagAsButton_cc125f'

lyric = [
    "",
    "Corrupt binary codes infecting my mind",
    "Perform invocation with numbing freeze",
    "Querying for a variable and seizing the time",
    "To recompile and trigger my destiny",
    "Though my wings've been bloodstained and could never rid",
    "I will try hard to soar to the heaven I dreamed",
    "There is no \"Exception\" in this library",
    "For I know I will always go with you",
    "",
    "Super hot projectiles pierce the wind",
    "I charged up my armor into light speed",
    "Querying for a variable and seizing the time",
    "In a new day coming not so far away",
    "Though my wings've been bloodstained and could never rid",
    "I will try hard to soar to the heaven I dreamed",
    "There is no \"Exception\" in this library",
    "For I know I will always go with you",
    "",
    "Though my wings've been bloodstained and could never rid",
    "I will try hard to soar to the heaven I dreamed",
    "There is no \"Exception\" in this library",
    "For I know I will always go with you",
    "Though my wings've been bloodstained and could never rid",
    "I will try hard to soar to the heaven I dreamed",
    "There is no \"Exception\" in this library",
    "For I know I will always go with my heart",
    ""
]

def recorrer_versos(versos):
    # Wait for the next page to load
    for verso in versos:
        for i in range(len(verso)):
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//section/div/div[contains(@class, 'avatarWrapper_ba5175') and contains(@aria-label, 'Establecer estado')]"))
            )
            #input = driver.find_element(By.CLASS_NAME, 'inputWrapper__934f5')
            #input.send_keys(verso[i:])
            print(verso[i:])
            #input = driver.find_element(By.CLASS_NAME, 'lookFilled__19298')
            BartraUtils.time.sleep(len(verso[i:])/2)


driver = webdriver.Edge()
driver.get("https://discord.com/login")
BartraUtils.time.sleep(10)
# Enter user
login_div = driver.find_element(By.CLASS_NAME, 'marginTop20_d88ee7')

username = login_div.find_element(By.ID, "uid_7")
username.send_keys("jedujakin16@gmail.com")

# Enter password
password = login_div.find_element(By.ID, "uid_9")
password.send_keys("Mimientacones")

button_submit = driver.find_element(By.XPATH, "//button/div[text()='Iniciar sesión']")
#button_submit = drive.find_element(By.XPATH, "//button[@ype='submit' and @class='button__47891']")
button_submit.click()

recorrer_versos(lyric)
