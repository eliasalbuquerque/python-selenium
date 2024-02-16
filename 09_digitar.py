# 202401 - Python 3.12.0
# 5.26 - Como DIGITAR naturalmente com selenium


import logging
import traceback
import random
from time import sleep
from app import iniciar_driver
from selenium.webdriver.common.by import By


def digitar_texto(driver, elemento, texto):
    logger = logging.getLogger(__name__)

    elemento = driver.find_element(By.XPATH, elemento)

    try:
        for letra in texto:
            elemento.send_keys(letra)
            sleep(random.randint(1, 5)/30)
        sleep(1)
    except Exception as e:
        logger.error(f'Erro ao digitar texto:\n- {type(e).__name__}: {e}'
            f'Stack trace: {traceback.format_exc()}'
        )
        print(f'Erro ao digitar texto: {type(e).__name__}')


def scroll_pagina(driver, pixels):
    logger = logging.getLogger(__name__)

    try:
        driver.execute_script("window.scrollTo(0, arguments[0]);", pixels)
        sleep(1)
    except Exception as e:
        logger.error(f'Erro ao rolar página:\n- {type(e).__name__}: {e}'
            f'Stack trace: {traceback.format_exc()}'
        )
        print(f'Erro ao rolar página: {type(e).__name__}')


def clicar_elemento(driver, elemento):
    logger = logging.getLogger(__name__)

    try:
        elemento = driver.find_element(By.XPATH, elemento)
        driver.execute_script("arguments[0].click();", elemento)
        sleep(1)
    except Exception as e:
        logger.error(f'Erro ao clicar no elemento:\n- {type(e).__name__}: {e}'
            f'Stack trace: {traceback.format_exc()}'
        )
        print(f'Erro ao clicar no elemento: {type(e).__name__}')


def digitando_texto_naturalmente():
    site = 'https://cursoautomacao.netlify.app/desafios'
    driver = iniciar_driver(site_url=site, detach=True)
    sleep(1)

    elemento = '//textarea[@id="campoparagrafo"]'
    validar = '//button[@onclick="ValidarDesafio4()"]'
    texto = '"A mudança não acontecerá se nós esperarmos por outra pessoa ou se esperarmos por algum outro momento. Nós somos as pessoas pelas quais esperávamos. Nós somos a mudança que buscamos."\nBarack Obama'

    scroll_pagina(driver, 1100)
    digitar_texto(driver, elemento, texto)
    clicar_elemento(driver, validar)

    # no caso de haver algum alerta na tela:
    try:
        # accept() para 'OK', dismiss() para 'Cancel'
        alert = driver.switch_to.alert
        alert.accept()
        sleep(1)
    finally:
        driver.close()

if __name__=='__main__':
    digitando_texto_naturalmente()