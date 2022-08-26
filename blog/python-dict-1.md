---
title: Python - Dicionários
description: Operações com dicionários
date: 2022-08-25
tags: [dict,def]
---
[Início](python-curso)

```python
# Criar um dicionário aninhado
dicionario = {
    'pt': {
        'casa': 'CASA',
        'cão': 'CACHORRO'
    },
    'en': {
        'casa': 'HOUSE',
        'cão': 'DOG'
    }
}

# Função que imprime o valor de uma chave no dicionário
def traduzir(lingua, palavra):
    print(dicionario[lingua][palavra])


traduzir('en', 'cão')
```