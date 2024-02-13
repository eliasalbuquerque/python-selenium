# 202401 - Python 3.12.0
# MA_5.6 - CÓDIGO BASE

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging.config
import traceback
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import *


# configurando logging:
logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)


def iniciar_driver(
    site_url=None, detach=False, headless=False, zoom_level=1.0):
    """ Configuracao e inicializacao do driver e do wait"""    
    
    logger = logging.getLogger(__name__)

    try:
        # 1 - Driver:

        
        # montando options:
        options = ChromeOptions()

        arguments = [
            '--block-new-web-contents',  # Bloqueia pop-ups
            '--disable-notifications',  # Desabilita notificacoes
            '--lang=pt-BR',  # Define o idioma de inicializacao em portugues
            '--no-default-browser-check',  # Desabilita a busca pelo browser default
            '--window-position=36,68',  # Define o posicionamento da janela
            '--window-size=700,600',  # Define a resolucao da janela larguraXaltura
            # '--incognito', # Inicia janela no modo anonimo
            # '--lang=en-US', # Define o idioma de inicializacao em ingles
        ]

        for argument in arguments:
            options.add_argument(argument)

        
        # configuracoes adicionais do options: 
        

        # rodar em segundo plano
        if headless == True:
            options.add_argument('--headless')

        # manter janela aberta
        if detach == True:
            options.add_experimental_option('detach', True)

        # desabilitar pop-up de navegador controlado por automacao
        options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])

        # configuracoes de downloads, notificacoes e senhas do chrome
        options.add_experimental_option('prefs', {
            # downloads: alterar o local de downloads de arquivos
            'download.default_directory': 'Downloads',
            # downloads: desabilitar a confirmacao de download
            'download.prompt_for_download': False,
            # downloads: permitir multiplos downloads
            'profile.default_content_setting_values.automatic_downloads': 1,
            # downloads: notificar o google crhome sobre alteracao
            'download.directory_upgrade': True,
            # notificacoes: desabilitar notificacoes
            'profile.default_content_setting_values.notifications': 2,
            # desabilitar o gerenciador de senhas do chrome
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False,
        })


        # montando o driver
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )


        # 2 - Wait:


        # montando wait
        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
            ]
        )


        # Iniciar site automaticamente:


        # abre o site, aplica o zoom
        driver.get(site_url)
        driver.execute_script(f'document.body.style.zoom="{zoom_level}"')
        

        return driver, wait


    except Exception as e:
        logger.error(f'ERRO: ao iniciar o driver\n- {type(e).__name__}: {e}')
        return None


if __name__ == '__main__':
    # iniciar_driver(detach=True)
    # iniciar_driver(site_url='https://facebook.com', sleep_mode=True)
    iniciar_driver(
        site_url='https://facebook.com', detach=True, zoom_level=.75)



def scroll_pagina(driver, pixels):
    """ Configuracao de scrollagem do site"""

    logger = logging.getLogger(__name__)

    try:
        driver.execute_script("window.scrollTo(0, arguments[0]);", pixels)
        sleep(1)
    except Exception as e:
        logger.error(f'Erro ao rolar página:\n- {type(e).__name__}: {e}'
            f'Stack trace: {traceback.format_exc()}'
        )
        print(f'Erro ao rolar página: {type(e).__name__}')

