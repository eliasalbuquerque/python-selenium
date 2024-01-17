# 202401 - Python 3.12.0
# 5.25 - Como CLICAR em CHECKBOX


import logging
import traceback
from time import sleep
from app import iniciar_driver
from selenium.webdriver.common.by import By


# DESAFIO 3

def clicar_checkbox():
    logger = logging.getLogger(__name__)

    def clicar_elemento(xpath):
        elemento = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].click();", elemento)
        sleep(1)
        return elemento

    def scroll_pagina(pixcels):
        driver.execute_script("window.scrollTo(0, arguments[0]);", pixcels)
        sleep(1)

    try:
        # navegar ate a pagina
        site = 'https://cursoautomacao.netlify.app/desafios'
        driver = iniciar_driver(site_url=site, detach=True)
        
        # rolar pagina ate desafio 3
        scroll_pagina(600)

        # marcar 'conversivel' e 'off road' 
        xp_conversivel = '//input[@id="conversivelcheckbox"]'
        xp_offroad = '//input[@id="offroadcheckbox"]'
        cb_conversivel = clicar_elemento(xp_conversivel)
        cb_offroad = clicar_elemento(xp_offroad)

        # checar se elementos foram marcados
        if cb_conversivel.is_selected() and cb_offroad.is_selected() == True:
            print('Checkbox confirmado')
            # driver.close()
        else:
            print(f'Elemento checkbox não foi marcado corretamente')
            driver.close()

    except Exception as e:
        logger.error(
            f'Ao clicar em um elemento:\n- {type(e).__name__}: {e}'
            f'Stack trace: {traceback.format_exc()}'
        )
        print(f'Erro ao clicar em um elemento: {type(e).__name__}')
        driver.close()


clicar_checkbox()