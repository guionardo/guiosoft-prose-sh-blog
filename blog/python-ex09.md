---
title: Python - Ex 09 - Validando entrada
description: Exercício
date: 2022-09-06
tags: [input,int,print,while,continue,break]
---
[Início](python-curso)


Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

```python
while True:
    texto = input('Informe valor:')
    try:
        nota = int(texto)
    except:
        print('Número inválido')
        continue
    if 0 <= nota <= 10:
        break
    print('Nota inválida')
```