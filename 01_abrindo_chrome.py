# 202401 - Python 3.12.0
# MA_5.2 - Instalação de ferramentas no Windows-MAC-Linux


# ABRINDO O CHROME
# Documentacao:
# https://selenium-python.readthedocs.io/getting-started.html


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# inicializando o webdriver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# navegar até um site
driver.get('https://facebook.com')
sleep(10)
