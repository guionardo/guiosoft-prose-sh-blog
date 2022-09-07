---
title: Python - Ex 16 - Média
description: Exercício
date: 2022-09-06
tags: [print,for,sum,len]
---
[Início](python-curso)


Faça um programa, com uma função, que calcula a média de uma lista. Funções embutidas que podem te ajudar:

* len(lista) -> calcula o tamanho da lista
* sum(lista) -> faz o somatório dos valores


```python
def media(lista):
  contador = 0
  soma = 0
  for numero in lista:
    soma += numero
    contador += 1
  return soma/contador


           

lista = [3,5,3,7,9,4]
print(lista, 'média=',media(lista))
```

Outro método, mais curto

```python
def media(lista):
  return sum(lista)/len(lista)
```