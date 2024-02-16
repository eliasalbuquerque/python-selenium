# 202401 - Python 3.12.0
# 5.31 - Como TIRAR PRINT (FOTOS) da tela


from app import iniciar_driver
from time import sleep

site = 'https://cursoautomacao.netlify.app/'
driver = iniciar_driver(site_url=site, detach=True, zoom_level=.65)
sleep(1)

driver.save_screenshot('Assets/tela.jpg')
sleep(1)

driver.close()
