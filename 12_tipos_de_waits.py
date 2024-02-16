# 202402 - Python 3.12.0
# 5.44 - Pausa por WAIT EXPLÍCITO



from time import sleep
from app import iniciar_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def wait_sleep():
    # iniciar drive
    site = 'https://www.google.com/travel/flights/'
    driver, wait = iniciar_driver(site, True, False, .65)


    # elemento visivel na tela
    driver.execute_script("window.scrollTo(0, arguments[0]);", 300)
    
    
    # NOTE: Wait sleep() aguarda x segundos para o elemento aparecer na tela 
    sleep(3)
    sugestao_de_voo = driver.find_element(
        By.XPATH,'(//div[@role="button"])[6]')


    # clicar no elemento
    driver.execute_script("arguments[0].click();", sugestao_de_voo)
    
    
    # encerrar sessão
    sleep(3)
    driver.close()



def wait_implicito():
    # iniciar drive
    site = 'https://www.google.com/travel/flights/'
    driver, wait = iniciar_driver(site, True, False, .65)


    # elemento visivel na tela
    driver.execute_script("window.scrollTo(0, arguments[0]);", 300)
    

    # NOTE: Wait implicito aguarda ate 10 segundos o elemento aparecer na tela
    driver.implicitly_wait(10)
    sugestao_de_voo = driver.find_element(
        By.XPATH,'(//div[@role="button"])[6]')


    # clicar no elemento
    driver.execute_script("arguments[0].click();", sugestao_de_voo)
    
    
    # encerrar sessão
    sleep(3)
    driver.close()



def wait_explicito():
    # iniciar drive
    site = 'https://www.google.com/travel/flights/'
    driver, wait = iniciar_driver(site, True, False, .65)


    # elemento visivel na tela
    driver.execute_script("window.scrollTo(0, arguments[0]);", 300)


    # NOTE: Wait explicito de 1 elemento
    sugestao_de_voo = wait.until(
        EC.visibility_of_element_located((
            By.XPATH, '(//div[@role="button"])[6]')))

    
    # NOTE: 
    # para uma lista de varios elementos:
    #   * EC.visibility_of_all_elements_located((By.XPATH, ''))
    # 
    # para um elemento clicavel:
    #   * EC.element_to_be_clickable((By.XPATH, ''))


    # clicar no elemento
    driver.execute_script("arguments[0].click();", sugestao_de_voo)
    
    
    # encerrar sessão
    sleep(3)
    driver.close()


wait_sleep()
wait_implicito()
wait_explicito()