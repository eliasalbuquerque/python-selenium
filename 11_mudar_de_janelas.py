# 202402 - Python 3.12.0
# 5.35 - Como MUDAR de JANELA

# Desafio 7
# clicar botao: abrir nova janela
# digitar algo na nova janela
# clicar em pesquisar
# fechar a nova janela
# digitar algo na janela anterior


import os
import random
from time import sleep
from app import iniciar_driver, scroll_pagina
from selenium.webdriver.common.by import By


# iniciar drive
site = 'https://cursoautomacao.netlify.app/desafios'
driver = iniciar_driver(site_url=site, detach=True, zoom_level=.65)
sleep(1)


# elemento visivel na tela
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(1)


# funcao: logica do programa
# salvar janela inicial
janela_inicial = driver.current_window_handle

# abrindo e interagindo com a nova janela
botao_nova_janela = driver.find_element(
    By.XPATH,'//button[@onclick="abrirJanelaDesafio()"]')
driver.execute_script("arguments[0].click();", botao_nova_janela)

janelas = driver.window_handles

for janela in janelas:
    if janela not in janela_inicial:
        driver.switch_to.window(janela)

# digitando no campo de opiniao da nova janela
campo_opiniao = driver.find_element(
    By.XPATH, '//textarea[@id="opiniao_sobre_curso"]')
sleep(1)

texto_opniao_txt = os.path.join('Assets', 'texto_opiniao.txt')

with open(texto_opniao_txt, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        for letra in linha:
            campo_opiniao.send_keys(letra)
            sleep(random.randint(1, 5)/30)
sleep(1)

# clicando no botao pesquisar
botao_pesquisar = driver.find_element(
    By.XPATH, '//button[@id="fazer_pesquisa"]')
sleep(1)

# fechar janela
driver.close()
sleep(1)


# digitando no campo desafio 7 da janela anterior
driver.switch_to.window(janela_inicial)

campo_desafio_7 = driver.find_element(
    By.XPATH, '//textarea[@name="campo_depoimento"]')
sleep(1)

depoimento = 'Excelente curso!'

for letra in depoimento:
    campo_desafio_7.send_keys(letra)
    sleep(random.randint(1, 5)/30)


# encerrar sessão
sleep(3)
driver.close()
