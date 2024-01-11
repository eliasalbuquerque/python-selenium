# 202401 - Python 3.12.0
# MA_5.13 - Encontre elementos com base na TAG


from app import iniciar_driver
from selenium.webdriver.common.by import By

# args:
# site = 'https://site/'
# detach = True
# sleep_mode = True
# zoom_level=.75
site = 'https://cursoautomacao.netlify.app/'
driver = iniciar_driver(site_url=site, detach=True, zoom_level=.75)


# buscando elementos
elementos_h1 = driver.find_element(By.TAG_NAME, 'h1')
elementos_h4 = driver.find_elements(By.TAG_NAME, 'h4')

if elementos_h1 is not None:
    print('elementos_h1 foi encontrado')
if elementos_h4 is not None:
    print('elementos_h4 foram encontrados')
