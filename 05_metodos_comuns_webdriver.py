# 202401 - Python 3.12.0
# MA_5-16 - Métodos mais comuns do webdriver


from app import iniciar_driver
from selenium.webdriver.common.by import By
from time import sleep


# args:
# site = 'https://site/'
# detach = True
# sleep_mode = True
# zoom_level=.75
site = 'https://facebook.com'
driver = iniciar_driver(site_url=site, detach=True, zoom_level=.75)


# metodos mais comuns do webdriver:

# driver.get(site_url) # navegar ate um site
# Nota: esse metodo ja esta incluso no modulo principal dentro da funcao

sleep(2)
driver.maximize_window() # maximizar janela
sleep(2)
driver.set_window_rect(width=800, height=600) # restaurar janela
sleep(2)
driver.refresh() # recarregar a pagina atual
sleep(2)
driver.get(driver.current_url) # recarrega a pagina atual
sleep(2)
driver.get('https://cursoautomacao.netlify.app/') # navegar ate um site
sleep(2)
driver.back() # voltar a pagina anterior
sleep(2)
driver.forward() # avanca para a pagina anterior
sleep(2)
print(driver.title) # obtem titulo da pagina
sleep(2)
print(driver.current_url) # obtem url da pagina atual
sleep(2)
print(driver.page_source) # obtem o codigo fonte da pagina atual
sleep(2)
print(driver.find_element(By.XPATH, "//a[@class='navbar-brand']").text)
print(driver.find_element(By.XPATH, "//a[@class='navbar-brand']").get_attribute("href"))
sleep(2)
driver.close() # fechar janela atual
