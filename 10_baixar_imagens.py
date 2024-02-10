# 202402 - Python 3.12.0
# 5.32 - Como BAIXAR IMAGENS de um site


from time import sleep
from app import iniciar_driver, scroll_pagina
from selenium.webdriver.common.by import By


# acessar o site'
site = 'https://cursoautomacao.netlify.app/'
# driver = iniciar_driver(site_url=site, detach=True, headless=True)
driver = iniciar_driver(site_url=site, detach=True)
# zoom_level=.65) # nao eh possivel tirar print com zoom menor
sleep(1)

# scroll ate o elemento
scroll_pagina(driver, 2900)

# encontra elementos
imagens = driver.find_elements(By.XPATH, '//img[@class="img-thumbnail"]')
sleep(1)

# loop baixar imagens
def baixar_imagens():
    contador = 1
    for imagem in imagens:
        with open(f'Assets/imagem-{contador}.jpg', 'wb') as arquivo:
            arquivo.write(imagem.screenshot_as_png)
            sleep(1)
        contador += 1
        # para scrollar para o lado sem ter que mexer na resolucao da pagina
        if contador == 3:
            driver.execute_script("window.scrollTo(400, 2900);")
            sleep(1)

baixar_imagens()

# encerrar sessao
driver.close() 
