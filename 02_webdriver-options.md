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
    '--enable-automation', # Habilita inficacao que o browser esta sendo controlado por automacao
    '--headless', # Roda em segundo plano (com janela fechada)
    '--incognito', # Inicia janela no modo anonimo
    '--lang=en-US', # Define o idioma de inicializacao em ingles 
    '--lang=pt-BR', # Define o idioma de inicializacao em portugues
    '--no-default-browser-check', # Desabilita a busca pelo browser default
    '--window-position=0,0', # Define o posicionamento da janela 
    '--window-size=600,600', # Define a resolucao da janela largura X altura
]
```


## Reference

https://peter.sh/experiments/chromium-command-line-switches/