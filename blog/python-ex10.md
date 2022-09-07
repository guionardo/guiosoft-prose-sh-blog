---
title: Python - Ex 10 - Maior número
description: Exercício
date: 2022-09-06
tags: [input,int,print,while,continue,break]
---
[Início](python-curso)


Faça um programa que leia 5 números e informe o maior número.

```python
maior = -999999
for n in range(5):
  numero = int(input(f'Número #{n+1}:'))
  if numero > maior:
    maior = numero

print('Maior =',maior)
```

Outro método, mais curto

```python
maior = max([int(input(f'Número #{n+1}:')) 
             for n in range(5)])
print('Maior =',maior)
```