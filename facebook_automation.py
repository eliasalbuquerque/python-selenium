"""
title: 'facebook_automation'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-02-09'
update: '2024-02-10'
"""

"""
Automatizando postagem no Facebook:
O programa abre um novo browser, faz o login na conta do usuário, abre o campo 
de postagem de status, digita a mensagem e posta a mensagem.
"""

import random
from time import sleep
from decouple import config
from app import iniciar_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# iniciar drive
def acessar_site(site):
    driver, wait = iniciar_driver(site_url=site, detach=True, zoom_level=.75)
    return driver
    sleep(random.randint(1, 5))

driver = acessar_site('https://www.facebook.com/')


# funcao: logica do programa
def digitar(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)
    sleep(random.randint(1, 5))


def fazer_login(login, senha, driver):
    '''
    Fazer um sistema de login que solicite o login e senha como input, pergunte 
    se o usuario deseja salvar e em seguida faz o login e no caso de não salvar 
    a senha, apagar a senha e o login digitado, no caso de salvar a senha, 
    salvar no arquivo .env 
    '''
    fill_login = driver.find_element(By.XPATH,'//input[@id="email"]')
    fill_pass = driver.find_element(By.XPATH,'//input[@id="pass"]')
    button_login = driver.find_element(By.XPATH,'//button[@name="login"]')
    
    driver.execute_script("arguments[0].click();",fill_login)
    sleep(random.randint(1, 5))
    digitar(login, fill_login)
    
    sleep(random.randint(1, 5))
    driver.execute_script("arguments[0].click();",fill_pass)
    sleep(random.randint(1, 5))
    digitar(senha, fill_pass)
    
    sleep(random.randint(1, 5))
    driver.execute_script("arguments[0].click();",button_login)
    sleep(random.randint(1, 5))


def fazer_postagem(texto, driver):
    sleep(2)
    button_fill_post = driver.find_element(By.XPATH,'//span[contains(text(), "What\'s on your mind, Elias?")]')
    sleep(2)
    driver.execute_script("arguments[0].click()", button_fill_post)

    sleep(2)
    fill_post = driver.find_element(By.XPATH,'//div[@aria-label="What\'s on your mind, Elias?"]')
    sleep(2)
    digitar(texto, fill_post)

    sleep(2)
    button_post = driver.find_element(By.XPATH,'//span[contains(text(),"Post")]')
    sleep(2)
    driver.execute_script("arguments[0].click()", button_post)
    sleep(random.randint(1, 5))


# main
FACEBOOK_LOGIN = config('FACEBOOK_LOGIN')
FACEBOOK_SENHA = config('FACEBOOK_SENHA')
fazer_login(login=FACEBOOK_LOGIN, senha=FACEBOOK_SENHA, driver=driver)

pensamento = 'Automatizando Facebook'
fazer_postagem(texto=pensamento, driver=driver)


# encerrar sessão
driver.close()