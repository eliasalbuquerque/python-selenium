# 202401 - Python 3.12.0
# MA_5.9 - Encontre elementos por NAME


from app import iniciar_driver
from selenium.webdriver.common.by import By

# args:
# site = 'https://site/'
# detach = True
# sleep_mode = True
# zoom_level=.75
site = 'https://cursoautomacao.netlify.app/'
driver = iniciar_driver(site_url=site, detach=True)


# buscando elementos
campo_nome = driver.find_element(By.NAME, 'seu-nome')
radio_buttons = driver.find_elements(By.NAME, 'exampleRadios')

if campo_nome is not None:
    print('campo nome foi encontrado')
if radio_buttons is not None:
    print('radio buttons foram encontrados')
