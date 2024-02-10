# 202402 - Python 3.12.0
# 5.33 - Como USAR teclas do TECLADO


from time import sleep
from app import iniciar_driver, scroll_pagina
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



# iniciar driver e iniciar actions
site = 'https://cursoautomacao.netlify.app/'
driver = iniciar_driver(site_url=site, detach=True, zoom_level=.75)
actions = ActionChains(driver)
sleep(1)


# encontrar o elemento
radio_button_windows = driver.find_element(
    By.XPATH,'//input[@id="WindowsRadioButton"]')
sleep(1)


# funcao: logica do programa

def tecla_down():
    # clicar no elemento:
    # radio_button_windows.click()  # essa merda nao funciona
    # driver.execute_script("arguments[0].click();", radio_button_windows)

    # NOTE: nao precisa clicar no elemento para utilizar outras teclas, mas 
    #       pode utilizar um elemento como referencia.

    # usando radio button windows como referencia para usar a tecla 'setinha 
    # para baixo' e deixar o elemento selecionado:
    radio_button_windows.send_keys(Keys.DOWN)
    sleep(1)

def tecla_tab():
    # usando redio button windows como referencia para usar a tecla 'tab' e 
    # selecionar outro elemento:
    radio_button_windows.send_keys(Keys.TAB)
    sleep(1)

def tecla_space():
    # usando a 'barra de espaco' para clicar no elemento selecionado previamente
    actions.send_keys(Keys.SPACE).perform()
    sleep(1)

def tecla_pagedown(n):
    for _ in range(n):
        actions.send_keys(Keys.PAGE_DOWN).perform()


tecla_down()
tecla_tab()
tecla_space()
tecla_pagedown(4)


# encerrar sessão
# driver.close()