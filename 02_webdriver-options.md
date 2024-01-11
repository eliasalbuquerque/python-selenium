# Arguments for Webdriver Options

This document is part of the `02_config_comportamento_do_browser.py` file.


## List of Chromium Command Line Switches


There are lots of command lines which can be used with the Google Chrome 
browser. Some change behavior of features, others are for debugging or 
experimenting. This page lists the available switches including their conditions 
and descriptions. Last automated update occurred on 2024-01-07.


```python
arguments = [
    '--block-new-web-contents', # Bloqueia pop-ups
    '--disable-notifications', # Desabilita notificacoes
    '--headless', # Roda em segundo plano (com janela fechada)
    '--incognito', # Inicia janela no modo anonimo
    '--lang=en-US', # Define o idioma de inicializacao em ingles 
    '--lang=pt-BR', # Define o idioma de inicializacao em portugues
    '--no-default-browser-check', # Desabilita a busca pelo browser default
    '--window-position=0,0', # Define o posicionamento da janela 
    '--window-size=600,600', # Define a resolucao da janela largura X altura
]
```


## Experimental Options


```python
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
```




## Reference

https://peter.sh/experiments/chromium-command-line-switches/