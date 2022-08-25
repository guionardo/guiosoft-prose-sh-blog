---
title: Python - Fluxo Condicional
description: Fluxo Condicional- if, elif e else
date: 2022-08-25
tags: [if,elif,else]
---
[Início](python-curso)

```python
n = int(input('Número?'))

if n > 5:
    # Testa se o número é maior que 5
    print(n, ' é maior do que 5')
    
    # O código aqui está aninhado no if anterior, 
    # então ele será executado em seguida
    if n > 100:
        print(n, 'é grande')
        # Mais um if aninhado
        if n > 1000:
            print(n, 'é muito grande')
elif n > 2:
    print(n, 'é maior do que 2')
else:
    print(n)
```