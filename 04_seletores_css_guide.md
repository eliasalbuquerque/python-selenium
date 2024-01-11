<!--
title: 'Seletores CSS para elementos DOM'
author: 'Elias Albuquerque'
created: '2024-01-11'
update: '2024-01-11'
-->


# Seletores CSS para elementos DOM

- tag (section,div,h4,button)
- class (.btn)
- combinação de class (.btn.btn-success)
- Id (#dropDownMenuButton)

Para encontrar valores exatos

```html
input[class='form-check-input']
```

Inicia com algum valor

```html
input[class^='form']
```

finaliza com algum valor

```html
input[class$='input']
```

Contem algum valor

```html
input[class*='check']
```