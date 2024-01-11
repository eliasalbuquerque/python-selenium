# 202401 - Python 3.12.0
# MA_5.14 - Guia completo do XPATH


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
elemento_xpath = driver.find_element(
    By.XPATH, "//h4[contains(text(),'Bootstrap')]")
elementos_xpath_filho_especifico = driver.find_elements(
    By.XPATH, "//thead/tr//th[2]")
elementos_xpath_filhos = driver.find_elements(
    By.XPATH, "//thead/tr//th")


# print
if elemento_xpath is not None:
    print(f'elemento_xpath foi encontrado: {elemento_xpath.text}')

if elementos_xpath_filho_especifico is not None:
    print('elementos_xpath_filho_especifico foi encontrado')
    
if elementos_xpath_filhos is not None:
    print('elementos_xpath foram encontrados')
    for elemento in elementos_xpath_filhos:
        print(f'{elemento.text}')

