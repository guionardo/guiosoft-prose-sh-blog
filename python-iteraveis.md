---
title: Python - Iteráveis
description: Operações com dicionários
date: 2022-08-25
tags: [iterable,str,set,list,dict]
---
[Início](python-curso)

```python
st = "STRING COM TAMANHO VARIÁVEL"
li = list([1,2,3,True,'A'])
se = set([1,2,3,True,'A'])
di = dict(nome='Guionardo',idade=45)
```

## Iteração por um string
```python
for item in st:
    # Código será executado para cada caracter do string
    print(item)
else:
    print('* FIM DA STRING*')    # Este código ocorre ao final da iteração
```

## Iteração por uma lista
```python
for item in li:
    # Código será executado para cada item da lista
    print(item)
else:
    print('* FIM DA LISTA*')    # Este código ocorre ao final da iteração
```

## Iteração por um set (conjunto)
```python
for item in se:
    # Código será executado para cada item do set
    print(item)
else:
    print('* FIM DO SET*')    # Este código ocorre ao final da iteração
```

## Iteração obtendo um índice e o valor
```python
for indice,item in enumerate(li):
    # O médoto enumerate vai iterar pela lista e a cada iteração
    # retornar uma tupla (indice,item) que pode ser desconstruída
    # informando as duas variáveis no for
    print(f'#{indice} = {item}')
```

## Iteração por um dict (dicionário)
```python
for item in di:
    # Código será executado para cada chave do dicionário
    print(item)
else:
    print('* FIM DO DICT')    # Este código ocorre ao final da iteração
```

## Iteração por um dict (obtendo chave e valor)
```python
for chave,valor in di.items():
    # o médoto items do dicionário vai entregar a cada iteração, 
    # uma tupla (chave,valor) que pode ser desconstruída 
    # informando as duas variáveis no for.
    print(f'{chave}={valor}')
else:
    print('* FIM DO DICT')
```

