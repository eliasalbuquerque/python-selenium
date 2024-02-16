# 202402 - Python 3.12.0
# 5.39 - Como simular AÇÕES comuns do MOUSE


# imports
# time, app, selenium: Select, By, Keys, ActionChains
from time import sleep
from app import iniciar_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def teste1():
    """rodando o script com o zoom out na pagina e corrigindo cliques nos elementos"""

    # iniciar drive
    site = 'https://cursoautomacao.netlify.app/exemplo_chains/'
    driver = iniciar_driver(site_url=site, detach=True, zoom_level=.65)
    actions = ActionChains(driver)


    # elemento visivel na tela
    botao_actions = driver.find_element(
        By.XPATH, '//button[@id="botao-direito"]')
    sleep(1)
    driver.execute_script("arguments[0].style.zoom = '1.5'", botao_actions)
    sleep(1)

    # NOTE: o script acima corrige o erro do clique causado pelo zoom out da 
    #       página em 65%, tirando a referencia do actions.clique(), nesse 
    #       caso, o zoom no no elemento foi corrigido com o zoom no proprio
    #       elemento botao de clique.


    # aplicando actions
    actions.context_click(botao_actions).pause(2)
    actions.send_keys(Keys.UP).pause(2)
    # actions.send_keys(Keys.DOWN).pause(2)
    # actions.send_keys(Keys.DOWN).pause(2)
    actions.click()
    actions.perform()
    sleep(3)

    # NOTE: apos a correcao do clique no elemento, o menu de contexto abre com 
    #       um dos elementos internos ja selecionado, causando erro na 
    #       sequencia de cliques e selecao do elemento correto a ser clicado. 
    #       A solucao foi alterar a sequencia e selecionar o elemento correto 
    #       de clique e performar conforme o desejado.

    try:
        # tenta aceitar o alerta
        driver.switch_to.alert.accept()
    finally:
        # encerrar sessão
        sleep(1)
        driver.close()

teste1()


def teste2():
    """rodando o script sem o zoom out na pagina"""
    
    # iniciar drive
    site = 'https://cursoautomacao.netlify.app/exemplo_chains/'
    driver = iniciar_driver(site_url=site, detach=True)
    actions = ActionChains(driver)


    # elemento visivel na tela
    botao_actions = driver.find_element(
        By.XPATH, '//button[@id="botao-direito"]')
    sleep(2)


    # aplicando actions
    actions.context_click(botao_actions).pause(2)
    actions.send_keys(Keys.DOWN).pause(2)
    actions.send_keys(Keys.DOWN).pause(2)
    actions.send_keys(Keys.DOWN).pause(2)
    actions.click().pause(1)
    actions.perform()
    sleep(2)

    try:
        # tenta aceitar o alerta
        driver.switch_to.alert.accept()
    finally:
        # encerrar sessão
        sleep(1)
        driver.close()

    # NOTE: por algum motivo, nesse modo o clique no elemento dentro do menu de 
    #       contexto, nao gera o alerta esperado de confirmacao de clique. 
    #       Provavelmente, o clique nao ocorre e o programa ignora o alerta, 
    #       fechando a janela.
    #       Ainda, nesse programa, foi testado o ajuste de offset de x e y, 
    #       porém, os resultados nao foram obtidos conforme o esperado. 
    #       Há uma divergencia entre o que o selenium enxerga no DOM e o que 
    #       ele faz no zoom out, que gera perda de referencia do elemento a ser 
    #       clicado e mesmo ajustando coordenadas, nao foi possivel executar a 
    #       acao do clique de maneira correta. 


teste2()
