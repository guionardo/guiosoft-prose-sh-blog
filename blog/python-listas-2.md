---
title: Python - Listas 02
description: Operações com listas
date: 2022-08-25
tags: [list,int,comprehension]
---
[Início](python-curso)

Podemos usar a função *list* para obter uma lista a partir de qualquer iterável.

## Criar uma lista de números em sequencia de 1 a 10
```python
lista_numeros = list(range(1,11))
print(lista_numeros)
```

```
[1,2,3,4,5,6,7,8,9,10]
```
## Criar uma lista dos caracteres de uma string

```python
letras = list('GUIONARDO')
print(letras)
```

```
['G','U','I','O','N','A','R','D','O']
```

```python
# perguntar ao usuário, um número entre 1 e 10 inclusive
#  e armazenar numa variável

n = int(input('Número de items: '))

# Criar uma lista de números em sequencia
# com tamanho igual ao número anterior

lista = list(range(1, n+1))

# Exibir a lista
print(lista)


# Criar uma nova lista, apenas com os números pares

lista_pares = [numero
               for numero in lista
               if numero % 2 == 0]

# Exibir a nova lista
print(lista_pares)

lista_multiplos_3 = [numero
                     for numero in lista
                     if numero % 3 == 0]
print(lista_multiplos_3)
```