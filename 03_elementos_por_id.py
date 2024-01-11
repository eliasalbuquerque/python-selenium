# 202401 - Python 3.12.0
# MA_5.8 - Encontre elementos por ID


from app import iniciar_driver
from selenium.webdriver.common.by import By

# args:
# site = 'https://site/'
# detach=True
# sleep_mode=True
# zoom_level=.75
site = 'https://cursoautomacao.netlify.app/'
driver = iniciar_driver(site_url=site, detach=True)


# buscando elementos
botao = driver.find_element(By.ID, 'buttonalerta')
botoes = driver.find_elements(By.ID, 'buttonalerta')

if botao is not None:
    print('botao foi encontrado')
if botoes is not None:
    print('botoes foram encontrados')
