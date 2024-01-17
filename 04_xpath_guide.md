<!--
title: 'Guia completo do XPATH'
author: 'Elias Albuquerque'
created: '2024-01-11'
update: '2024-01-11'
-->


# Guia completo do XPath


De forma geral, a sintaxe do `XPath` é:

```html
//tag[@atributo="valor"]
```

Para utilizar o `XPath`, abra o navegador e tecle `F12`, em seguida, `ctrl+f`:

![xpath-find](Assets\xpath-find.png)


## Tipos de pesquisa

Ultra genérico (engloba todas as tags da página):
```html
//* 
```

Ultra genérico + tag:
```html
//*[tag]
```

Encontrar elementos que contém apenas parte do texto:
```html
//*[contains(text(),"Exemplo")] 
//*[contains(text(),"Exemplo") or contains( text(), "Dropdown" )]
//*[contains(text(),'Dropdown') and  contains(text(),'Bootstrap') ]
```

Elementos que inicia com um texto:
```html
//*[starts-with(text(),"Exemplo")]
//*[starts-with(@class,"btn")]
```

Buscando apenas por um texto spefícico:
```html
//*[text()="Exemplo Checkbox"] # Genérico, porém especificando o texto
//h4[text()="Exemplo Checkbox"] # Com tag e especificando o texto
```

Buscando por um elemento específico usando tag e propriedade:
```html
//button[@id="dropdownMenuButton"] # tag com propriedade e valor
//section[@class="jumbotron"] # tag com propriedade e valor
//div[@class="form-check"] #tag com propriedade e valor
```

## Como encontrar filhos de cada elemento

Encontra filho único:
```html
//div/fieldset
//div/fieldset/h4
//div[@id='select-class-example']/fieldset/h4
```

Encontrar filho, quando há multiplos filhos:
```html
//thead/tr//th[2]
```


---


## Para mais funções do `XPath`:

**Source**: Conversation with Bing, 1/11/2024

XPath has a wide range of functions and attributes that you can use, similar to `text()` and `@class`. Here are some of them:

1. `contains()`: Checks if a string contains a specific substring¹.
2. `starts-with()`: Checks if a string starts with a specific substring¹.
3. `boolean()`: Converts an argument to a boolean¹.
4. `ceiling()`: Rounds a number up to the nearest integer¹.
5. `concat()`: Concatenates two or more strings¹.
6. `count()`: Returns the count of nodes selected by a given XPath expression¹.
7. `current()`: Returns the current node¹.
8. `false()`: Returns false¹.
9. `floor()`: Rounds a number down to the nearest integer¹.
10. `id()`: Selects elements based on their id¹.
11. `last()`: Selects the last node of the selected context¹.
12. `name()`: Returns the name of the current node¹.
13. `normalize-space()`: Strips leading and trailing white-space from a string, replaces sequences of whitespace characters by a single space, and returns the resulting string¹.
14. `not()`: Returns true if the argument is false, and false otherwise¹.
15. `number()`: Converts an argument to a number¹.
16. `position()`: Returns the position of the current node in the context¹.
17. `round()`: Rounds a number to the nearest integer¹.
18. `string()`: Converts an argument to a string¹.
19. `string-length()`: Returns the number of characters in a string¹.
20. `substring()`: Returns a part of a string¹.
21. `substring-after()`: Returns the substring after the first occurrence of a delimiter¹.
22. `substring-before()`: Returns the substring before the first occurrence of a delimiter¹.
23. `sum()`: Returns the sum of a sequence of numbers¹.
24. `translate()`: Replaces some characters with some other characters in a string¹.
25. `true()`: Returns true¹.

These are just a few examples. XPath contains over 200 built-in functions². For more detailed information, you can refer to this [XPath Functions Reference](^1^).

### Reference

(1) Functions - XPath | MDN - MDN Web Docs. [developer.mozilla.org/XPath/Functions](https://developer.mozilla.org/en-US/docs/Web/XPath/Functions).

(2) XPath Tutorial - W3Schools. [www.w3schools.com/xpath_intro](https://www.w3schools.com/xml/xpath_intro.asp).