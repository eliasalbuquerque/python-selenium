
# 202401 - Python 3.12.0
# MA_5.15 - Guia completo de seletores CSS


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
elemento_h1 = driver.find_element(By.CSS_SELECTOR,'h1')
elementos_form_chec = driver.find_element(By.CSS_SELECTOR,'input[class="form-check-input"]')


# print
if elemento_h1 is not None:
    print('elemento_h1 foi encontrado')
if elementos_form_chec is not None:
    print('elementos_form_chec foram encontrados')
