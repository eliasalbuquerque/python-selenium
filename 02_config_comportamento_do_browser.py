# 202401 - Python 3.12.0
# MA_5.5 - Como alterar como o navegador deve se portar


# Definir as opcoes de inicializacao do Chrome:
# 1. importar classe Options() de selenium webdriver chrome
# 2. Definir funcionalidades especificas do Chrome:
# 3. Inserindo lista de argumentos em options
# 4. Adicionando configuracoes experimentais:
# 5. Inserir `options` na inicializacao do webdriver


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# 1. importar classe Options() de selenium webdriver chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


# 2. Definir funcionalidades especificas do Chrome:
# DOC: https://www.selenium.dev/documentation/webdriver/browsers/chrome/
options = ChromeOptions()


# 3. Inserindo lista de argumentos em options
arguments = [
    '--block-new-web-contents',  # Bloqueia pop-ups
    '--disable-notifications',  # Desabilita notificacoes
    # Habilita inficacao que o browser esta sendo controlado por automacao
    # '--enable-automation',
    # '--lang=pt-BR', # Define o idioma de inicializacao em portugues
    '--lang=en-US',  # Define o idioma de inicializacao em portugues
    '--no-default-browser-check',  # Desabilita a busca pelo browser default
    '--window-position=100,100',  # Define o posicionamento da janela
    '--window-size=700,600',  # Define a resolucao da janela larguraXaltura
]
# NOTE:
# For more switches, please read the `02_webdriver-options.md`

for argument in arguments:
    options.add_argument(argument)


# 4. Adicionando configuracoes experimentais:

    # manter a janela aberta apos o script
options.add_experimental_option('detach', True)

    # desabilitar pop-up de navegador controlado por automacao
options.add_experimental_option('excludeSwitches', ['enable-automation'])

    # setar preferencias do navegador:
options.add_experimental_option('prefs', {
    # downloads: alterar o local de downloads de arquivos
    'download.default_directory': 'C:\\path\\to\\download',
    # downloads: notificar o google crhome sobre alteracao
    'download.directory_upgrade': True,
    # downloads: desabilitar a confirmacao de download
    'download.prompt_for_download': False,
    # downloads: permitir multiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,
    # notificacoes: desabilitar notificacoes
    'profile.default_content_setting_values.notifications': 2,
})


# 5. Inserir `options` na inicializacao do webdriver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)


# navegar até um site
driver.get('https://facebook.com')


# manter a janela ativa por x segundos
# sleep(10)
