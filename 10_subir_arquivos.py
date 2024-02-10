# 202401 - Python 3.12.0
# 5.30 - Como SUBIR ARQUIVOS usando Seleinum


from time import sleep
from app import iniciar_driver, scroll_pagina
from selenium.webdriver.common.by import By


# ir ate o elemento 'escolher arquivo'
site = 'https://cursoautomacao.netlify.app/'
driver = iniciar_driver(site_url=site, detach=True, zoom_level=.65)

# arquivo para subir no site
caminho_do_arquivo = r"C:\Users\elias\Workspace\python-selenium\Assets\New Text Document.txt"
sleep(2)
scroll_pagina(driver, 2500)

# encontrar botao para envio do arquivo
xpath_escolher_arquivo = '//input[@id="myFile"]'
botao_escolher_arquivo = driver.find_element(By.XPATH, xpath_escolher_arquivo)
sleep(1)

# subir arquivo
botao_escolher_arquivo.send_keys(caminho_do_arquivo)
sleep(1)

# clicar botao enviar
xpath_enviar = '//input[@value="Enviar Arquivo"]'
botao_enviar = driver.find_element(By.XPATH, xpath_enviar)
driver.execute_script("arguments[0].click();", botao_enviar)
sleep(2)

# clicar no alerta de confirmacao de envio
alerta = driver.switch_to.alert
alerta.accept()
sleep(2)

# encerrar sessao
driver.close()