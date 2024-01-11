# 202401 - Python 3.12.0
# MA_5.2 - Instalação de ferramentas no Windows-MAC-Linux


# ABRINDO O FIREFOX
# Documentacao:
# https://selenium-python.readthedocs.io/getting-started.html


import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# inicializando o webdriver
driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))

# navegar até um site
driver.get('https://facebook.com')
time.sleep(10)
