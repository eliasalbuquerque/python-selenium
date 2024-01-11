# 202401 - Python 3.12.0
# MA_5.10 - Encontre elementos por CLASS NAME


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
logo = driver.find_element(By.CLASS_NAME, 'navbar-brand')
menus = driver.find_elements(By.CLASS_NAME, 'nav-link')

if logo is not None:
    print('logo foi encontrado')
if menus is not None:
    print('menus foram encontrados')
