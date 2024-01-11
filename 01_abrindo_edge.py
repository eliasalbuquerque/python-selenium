# 202401 - Python 3.12.0
# MA_5.2 - Instalação de ferramentas no Windows-MAC-Linux


# ABRINDO O EDGE
# Documentacao:
# https://selenium-python.readthedocs.io/getting-started.html


import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# inicializando o webdriver
driver = webdriver.Edge(service=EdgeService(
    EdgeChromiumDriverManager().install()))

# navegar até um site
driver.get('https://facebook.com')
time.sleep(10)
