# 202401 - Python 3.12.0
# MA_5.22 - Como CLICAR em BOTÕES E LINKS


import logging
import traceback
from time import sleep
from app import iniciar_driver
from selenium.webdriver.common.by import By



def clicar_links_botoes():
    logger = logging.getLogger(__name__)
    try:
        # entrar no site
        site = 'https://cursoautomacao.netlify.app/'
        driver = iniciar_driver(site_url=site, zoom_level=.75, detach=True)
        sleep(2)

        # clicar em login
        try:
            # se a tela estiver pequena e o login estiver dentro do menu
            xpath_botao_menu = "//button[@data-target='#navbarsExample04']"
            botao_menu = driver.find_element(By.XPATH, xpath_botao_menu)
            driver.execute_script("arguments[0].click();", botao_menu)
            sleep(2)
        finally:
            # clicar no botao login
            xpath_botao_login = "//a[@href='/login']"
            botao_login = driver.find_element(By.XPATH, xpath_botao_login)
            driver.execute_script("arguments[0].click();", botao_login)
            sleep(2)

        # digitar email no campo email
        xpath_email = "//input[@id='email']"
        campo_email = driver.find_element(By.XPATH, xpath_email)
        campo_email.send_keys('meu_email@example.com')
        sleep(2)
        
        # digitar senha e enviar
        xpath_senha = "//input[@id='senha']"
        campo_senha = driver.find_element(By.XPATH, xpath_senha)
        campo_senha.send_keys('1234', Keys.ENTER)
        sleep(2)

        driver.close()

    except Exception as e:
        logger.error(
            f'Ao clicar em um elemento:\n- {type(e).__name__}: {e}'
            f'Stack trace: {traceback.format_exc()}'
        )
        print(f'Erro ao clicar em um elemento: {type(e).__name__}')
        driver.close()

# clicar_links_botoes()


# DESAFIO 2

def desafio_2():
    logger = logging.getLogger(__name__)

    def clicar_elemento(xpath):
        elemento = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].click();", elemento)
        sleep(1)

    def preencher_elemento(xpath, preencher):
        elemento = driver.find_element(By.XPATH, xpath)
        elemento.send_keys(preencher)
        sleep(1)

    def scroll_pagina(valor):
        driver.execute_script("window.scrollTo(0, arguments[0]);", valor)
        sleep(1)

    site = 'https://cursoautomacao.netlify.app/'
    xpath_menu = '//button[@data-target="#navbarsExample04"]'
    xpath_desafio = '//a[@href="/desafios"]'
    nome = 'Elias Albuquerque'
    xp_dadosusuario = '//input[@id="dadosusuario"]'
    xp_cliqueaqui = '//button[@id="desafio2"]'
    xpath_validar = '//input[@id="escondido"]'
    xp_botao_validar = '//button[@id="validarDesafio2"]'
    
    try:
        '''
        preencher_elemento(elemento, xpath, preencher):
        clicar_elemento(elemento, xpath):
        scroll_pagina(valor):
        '''

        # nagegar ate o site
        driver = iniciar_driver(site_url=site, detach=True)
        sleep(1)

        try:
            clicar_elemento(xpath_menu)
        finally:
            clicar_elemento(xpath_desafio)

        # rolar janela
        scroll_pagina(485)

        # acessar campo de preenchimento desafio 2
        # preencher o nome
        preencher_elemento(xpath=xp_dadosusuario, preencher=nome)

        # clicar no botao 'clique aqui'
        clicar_elemento(xp_cliqueaqui)
        sleep(2)

        # desafio 2 bonus: campo escondido
        try:
            preencher_elemento(xpath=xpath_validar, preencher=nome)
            clicar_elemento(xp_botao_validar)
        finally:
            sleep(5)
            driver.close()

    except Exception as e:
        logger.error(
            f'Ao clicar em um elemento:\n- {type(e).__name__}: {e}'
            f'Stack trace: {traceback.format_exc()}'
        )
        print(f'Erro ao clicar em um elemento: {type(e).__name__}')
        driver.close()


desafio_2()