# 202402 - Python 3.12.0
# 5.38 - Como lidar com ALERTAS


# imports
# time, app, selenium: Select, By, Keys, ActionChains
from time import sleep
from app import iniciar_driver, scroll_pagina
from selenium.webdriver.common.by import By
import random


# iniciar drive
site = 'https://cursoautomacao.netlify.app/'
driver = iniciar_driver(site_url=site, detach=True, zoom_level=.65)
sleep(1)


# elemento visivel na tela
scroll_pagina(driver, 1000)


# solucao
def clicar_elemento(xpath):
    elemento = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].click();", elemento)
    sleep(1)
    return elemento

def digitar_texto(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)


# situacao 1: alerta
# digitar meu nome
def digitar_meu_nome():
    campo_nome = clicar_elemento('//input[@id="nome"]')
    digitar_texto('Elias', campo_nome)

digitar_meu_nome()

# clicar em alerta
botao_alerta = clicar_elemento('//input[@id="buttonalerta"]')
sleep(2)

# no alerta, clicar em ok para fechar alerta
driver.switch_to.alert.accept()
sleep(2)

# situacao 2: alerta confirma (ok  e cancelar)
# digitar meu nome
digitar_meu_nome()

# clicar em confirmar (cancelar)
def clicar_em_confirmar():
    botao_confirmar = clicar_elemento('//input[@id="buttonconfirmar"]')
    sleep(2)

clicar_em_confirmar()

# no alerta, clicar em cancelar
driver.switch_to.alert.dismiss()
sleep(2)

# situacao 3: alerta pergunta
# clicar em fazer pergunta
botao_pergunta = clicar_elemento('//input[@id="botaoPrompt"]')
sleep(2)

# no alerta, responder que dia e hoje
driver.switch_to.alert.send_keys('Sábado')
sleep(2)

# no alerta, clicar em ok
driver.switch_to.alert.accept()
sleep(1)

# no ultimo alerta, clicar em ok
driver.switch_to.alert.accept()
sleep(1)

# encerrar sessão
driver.close()
