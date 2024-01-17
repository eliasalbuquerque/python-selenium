# 202401 - Python 3.12.0
# MA_5.20 - Como fazer SCROLL-ROLAR a página


import logging
from app import iniciar_driver
from selenium.webdriver.common.by import By
from time import sleep


def rolando_a_pagina():
    logger = logging.getLogger(__name__)
    try:
        # args:
        # site = 'https://site/'
        # detach = True
        # sleep_mode = True
        # zoom_level=.75
        site = 'https://cursoautomacao.netlify.app/'
        driver = iniciar_driver(site_url=site, detach=True, zoom_level=.75)

        sleep(2)
        # rolar ate o fim da pagina
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(2)
        # rolar ate o topo da pagina
        driver.execute_script('window.scrollTo(0, document.body.scrollTop);')
        sleep(2)
        # rolar x quantidade de pixels para baixo
        driver.execute_script('window.scrollTo(0, 1500);')
        sleep(2)
        # rolar x quantidade de pixels para cima
        driver.execute_script('window.scrollTo(0, -1500);')
        sleep(2)

        driver.close()

    except Exception as e:
        logger.error(
            f'Nao foi possivel usar a funcao rolando_a_pagina()\n- {type(e).__name__}: {e}')


# rolando_a_pagina()


def desafio_scroll():
    logger = logging.getLogger(__name__)
    try:
        site = 'https://cursoautomacao.netlify.app/desafios'
        driver = iniciar_driver(site_url=site, detach=True, zoom_level=.75)

        # rolar para o final da pagina
        sleep(2)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        # rolar para o inicio da pagina
        sleep(2)
        driver.execute_script('window.scrollTo(0, document.body.scrollTop);')

        sleep(2)
        driver.close()

    except Exception as e:
        logger.error(
            f'Nao foi possivel usar a funcao desafio_scroll()\n- {type(e).__name__}: {e}')


desafio_scroll()