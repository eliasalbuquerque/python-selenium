# 202401 - Python 3.12.0
# MA_5-21 - 2 Maneiras de clicar em um elemento


import logging
import traceback
from time import sleep
from app import iniciar_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# 1. Utilizando o método webdriver click():
def clicar_elemento_1():
    logger = logging.getLogger(__name__)
    try:
        # acessa o site
        site = 'https://cursoautomacao.netlify.app/'
        driver = iniciar_driver(site_url=site, detach=True, zoom_level=.75)

        # encontra o elemento
        xpath_element = "//button[@class='btn btn-success dropdown-toggle']"

        # aguarda o elemento estar visivel na janela
        wait = WebDriverWait(driver, 10)
        botao_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_element)))

        # clicando atraves de metodo webdriver click()
        botao_dropdown.click()
        
        sleep(3)
        driver.close()

    except Exception as e:
        logger.error(
            f'Nao foi possivel clicar no elemento:\n- {type(e).__name__}: {e}\n'
            f'Stack trace: {traceback.format_exc()}'
        )


clicar_elemento_1()



# 2. Utilizando um script em javascript para clicar no botao:
def clicar_elemento_2():
    logger = logging.getLogger(__name__)
    try:
        # acessa o site
        site = 'https://cursoautomacao.netlify.app/'
        driver = iniciar_driver(site_url=site, detach=True, zoom_level=.75)

        # encontra o elemento
        xpath_element = "//button[@class='btn btn-success dropdown-toggle']"
        botao_dropdown = driver.find_element(By.XPATH, xpath_element)

        # clicando atraves de um script javascript
        driver.execute_script('arguments[0].click()', botao_dropdown)

        sleep(3)
        driver.close()

    except Exception as e:
        logger.error(
            f'Nao foi possivel clicar no elemento:\n- {type(e).__name__}: {e}'
            f'Stack trace: {traceback.format_exc()}'
        )


clicar_elemento_2()