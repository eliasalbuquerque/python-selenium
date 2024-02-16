"""
title: 'instagram_automation'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-02-14'
update: '2024-02-14'
"""


import random
from time import sleep
from app import iniciar_driver
from decouple import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def carregar_driver_wait_actions(site):
    # Inicializa o driver e o wait
    driver, wait = iniciar_driver(
        site_url=site, detach=True, headless=False, zoom_level=1.0)
    # Cria um objeto ActionChains
    actions = ActionChains(driver)
    return driver, wait, actions


def elemento_visivel(xpath, of_element=False, all_elements=False, any_elements=False, element_clickable=False):
    if of_element:
        elemento = wait.until(
            EC.visibility_of_element_located((
                By.XPATH, xpath)))
    elif all_elements:
        elemento = wait.until(
            EC.visibility_of_all_elements_located((
                By.XPATH, xpath)))
    elif any_elements:
        elemento = wait.until(
            EC.visibility_of_any_elements_located((
                By.XPATH, xpath)))
    elif element_clickable:
        elemento = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, xpath)))
    sleep(1)
    return elemento


def digitar_texto(elemento, texto):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 8)/30)
    sleep(1)


def login_instagram():
    campo_login = elemento_visivel(
        '//input[@name="username"]', of_element=True)
    digitar_texto(campo_login, LOGIN)

    campo_senha = elemento_visivel(
        '//input[@name="password"]', of_element=True)
    digitar_texto(campo_senha, SENHA)

    botao_entrar = elemento_visivel(
        '//div[contains(text(), "Entrar")]', of_element=True)
    driver.execute_script("arguments[0].click();", botao_entrar)


def curtir_postagem(pagina):
    # se elemento visivel vai para a pagina da curtida
    elemento_visivel(
        f'//img[@alt="Foto do perfil de {USUARIO}"]', of_element=True)
    sleep(2)
    driver.get(pagina)
    sleep(4)


    # abre ultima_postagem
    actions.send_keys(Keys.PAGE_DOWN).pause(1).perform()
    # post = elemento_visivel("//*[@crossorigin='anonymous' and @style='object-fit: cover;']", element_clickable=True)
    post = elemento_visivel('//div[@class="_aagw"]', element_clickable=True)
    
    driver.execute_script("arguments[0].click();", post)
    sleep(1)


    # verificar se ja foi curtida
    try:
        elemento = driver.find_element(By.XPATH, '(//div[@role="presentation" and @tabindex="-1"]//div[@role="button"]//span[@class]//*[contains(text(), "Descurtir")])[1]')
        verifica_curtida = False
    except NoSuchElementException:
        verifica_curtida = True

    if verifica_curtida:
        botao_curtir = elemento_visivel('//div[@role="presentation" and @tabindex="-1"]//div[@role="button"]//div//span[@class]', all_elements=True)
        driver.execute_script("arguments[0].click()", botao_curtir[0])

    sleep(1)
    actions.send_keys(Keys.ESCAPE).perform()

    # se sim, aguardar 24h e repetir o processo
    # usar o Agendador de Tarefas do Windows para rodar o app uma vez por dia


LOGIN = config('INSTAGRAM_LOGIN')
SENHA = config('INSTAGRAM_SENHA')
USUARIO = config('INSTAGRAM_USUARIO')


driver, wait, actions = carregar_driver_wait_actions(
    'https://www.instagram.com/')
login_instagram()
curtir_postagem('https://www.instagram.com/diolinux/')
# curtir_postagem('https://www.instagram.com/cursoemvideo/')

sleep(3)
driver.close()
