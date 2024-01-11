# 202401 - Python 3.12.0
# MA_5.11 - Encontre elementos por TEXTO em LINKS
# MA_5.12 - Encontre elementos puramente por TEXTO


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
link_home = driver.find_element(By.LINK_TEXT, 'Home')
link_parcial = driver.find_element(By.PARTIAL_LINK_TEXT, 'Des')
texto_puro = driver.find_element(By.XPATH, "//*[text()='ZONA DE TESTES']")


if link_home is not None:
    print('link_home foi encontrado')
if link_parcial is not None:
    print(f'link_parcial foi encontrado: {link_parcial.text}')
if texto_puro is not None:
    print(f'texto_puro foi encontrado: {texto_puro.text}')
