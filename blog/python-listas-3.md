---
title: Python - Listas 03
description: Operações com listas
date: 2022-08-25
tags: [list,set,comprehension,range]
---
[Início](python-curso)

## List Comprehension

Um recurso valioso do python é poder gerar sequencias usando *comprehension*.

Por exemplo, precisamos extrair os números pares de uma lista.

Da forma tracidional, faríamos:

```python
# Criamos uma lista com a origem dos dados
lista_numeros = list(range(0,20))
# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

# Criamos uma nova lista vazia
lista_numeros_pares = []

# Iteramos pelos itens da primeira lista
for numero in lista_numeros:
    if numero % 2 == 0:     # Se o número for divisível por 2, é par
        # Adicionamos o número ao final da lista
        lista_numeros_pares.append(numero)

print(lista_numeros_pares)
# [0,2,4,6,8,10,12,14,16,18]
```

Usando *list comprehension* faríamos o seguinte:

```python
lista_numeros_pares = [numero   # Número que será inserido na lista
                       for numero in lista_numeros # Laço de iteração dos números da lista
                       if numero %2 == 0    # Condição para verificar os números pares
                       ]

print(lista_numeros_pares)
# [0,2,4,6,8,10,12,14,16,18]
```
