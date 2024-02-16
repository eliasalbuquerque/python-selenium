# 202401 - Python 3.12.0
# 5.28 - Como INTERAGIR com DROPDOWN


from time import sleep
from app import iniciar_driver, scroll_pagina
from selenium.webdriver.common.by import By
# modulo para selecionar opcoes de indices de elementos
from selenium.webdriver.support.select import Select


site = 'https://cursoautomacao.netlify.app/desafios'
driver = iniciar_driver(site_url=site, detach=True, zoom_level=.75)
sleep(1)

scroll_pagina(driver, 1600)


paises_dropdown = driver.find_element(By.XPATH, '//select[@id="paisesselect"]')
opcoes = Select(paises_dropdown)

def selecionar_por_indice():
    opcoes.select_by_index(2)
    sleep(1)
    opcoes.select_by_index(4)
    sleep(1)
    opcoes.select_by_index(6)
    sleep(1)

# selecionar_por_indice()


def selecionar_por_valor():
    opcoes.select_by_value('estadosunidos')
    sleep(1)
    opcoes.select_by_value('africa')
    sleep(1)
    opcoes.select_by_value('chille')
    sleep(1)

# selecionar_por_valor()


def selecionar_por_texto_visivel():
    opcoes.select_by_visible_text('Estados Unidos')
    sleep(1)
    opcoes.select_by_visible_text('Africa')
    sleep(1)
    opcoes.select_by_visible_text('Chille')
    sleep(1)

selecionar_por_texto_visivel()



sleep(2)
driver.close()