# 202401 - Python 3.12.0
# MA_5.19 - Como saber se um elemento está habilitado


import logging
from app import iniciar_driver
from selenium.webdriver.common.by import By


def elemento_habilitado():
    logger = logging.getLogger(__name__)
    try:
        # args:
        # site = 'https://site/'
        # detach = True
        # sleep_mode = True
        # zoom_level=.75
        site = 'https://cursoautomacao.netlify.app/'
        driver = iniciar_driver(site_url=site, detach=True, zoom_level=.75)

        # acessa o iframe do elemento para poder acessar o elemento:
        driver.switch_to.frame(driver.find_element(
            By.XPATH, "//iframe[@src='https://cursoautomacao.netlify.app/desafios.html']"))

        # busca os elementos pelo elemento pai:
        botoes = driver.find_elements(
            By.XPATH, "//section[@class='jumbotron desafios1']/button")

        # depois itera sobre os elementos filhos:
        for botao in botoes:
            if botao.is_enabled():
                print(f'Botão habilitado: {botao.text}.')
            else:
                print(f'{botao.text} esta desabilitado!')

        # fecha o navegador
        driver.close()

    except Exception as e:
        logger.error(
            f'Ao tentar verificar elementos habilitados\n- {type(e).__name__}: {e}')


elemento_habilitado()
