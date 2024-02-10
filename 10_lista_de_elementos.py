# 202401 - Python 3.12.0
# 5.27 - Como INTERAGIR com LISTA DE ELEMENTOS


# DESAFIO 5 
# Marque apenas "carro 2, 4 e 5"
# Iterar sobre os elementos clicaveis


import logging
import traceback
from time import sleep
from app import iniciar_driver
from selenium.webdriver.common.by import By


def scroll_pagina(driver, pixels):
    logger = logging.getLogger(__name__)

    try:
        driver.execute_script("window.scrollTo(0, arguments[0]);", pixels)
        sleep(1)        

    except Exception as e:
        logger.error(f'Erro ao rolar pagina:\n- {type(e).__name__}: {e}'
            f'Stack trace: {traceback.format_exc()}'
        )
        print(f'Erro ao rolar pagina: {type(e).__name__}')


def clicar_elemento(driver, elemento):
    logger = logging.getLogger(__name__)

    try:
        driver.execute_script("arguments[0].click();", elemento)
        sleep(1)

    except Exception as e:
        logger.error(f'Erro ao clicar no elemento:\n- {type(e).__name__}: {e}'
            f'Stack trace: {traceback.format_exc()}'
        )
        print(f'Erro ao clicar no elemento: {type(e).__name__}')


def clicar_lista_elementos(driver, xpath):
    logger = logging.getLogger(__name__)

    # for elements lenght, click
    try:
        elementos = driver.find_elements(By.XPATH, xpath)
        for elemento in elementos:
            driver.execute_script("arguments[0].click();", elemento)
            sleep(.3)

    except Exception as e:
        logger.error(f'Erro ao iterar sobre os elementos:\n- {type(e).__name__}: {e}'
            f'Stack trace: {traceback.format_exc()}'
        )
        print(f'Erro ao iterar sobre os elementos: {type(e).__name__}')


def clicando_em_checkboxes():
    site = 'https://cursoautomacao.netlify.app/desafios'
    driver = iniciar_driver(site_url=site, detach=True, zoom_level=.75)
    sleep(1)

    scroll_pagina(driver, 1200)
    
    # Marque apenas "carro 2, 4 e 5"
    xpath_carros = '//input[@name="carros"]'
    elementos_carros = driver.find_elements(By.XPATH, xpath_carros)
    clicar_elemento(driver, elementos_carros[1])
    clicar_elemento(driver, elementos_carros[3])
    clicar_elemento(driver, elementos_carros[4])
    
    # Iterar sobre os elementos clicaveis
    xpath_motos = '//input[@name="motos"]'
    clicar_lista_elementos(driver, xpath_motos)


if __name__ == '__main__':
    clicando_em_checkboxes()