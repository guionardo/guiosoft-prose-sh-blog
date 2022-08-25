---
title: Python - range
date: 2022-08-25
tags: [range,for]
---
[Início](python-curso)

*range* é uma função interna do python que retorna um enumerável de números em sequencia, para ser usado em loops ou como produção de dados.

São três maneiras que se pode utilizar o range

## Sequencia simples

range(5) vai retornar um enumerador iniciando em 0 e entregando 5 números: 0, 1, 2, 3, 4.

ATENÇÃO: **Lembre-se que o número 5 não será entregue, pois começamos a enumerar a partir de zero.**

## Sequencia com início e fim:

range(3,9) vai retornar um enumerador iniciando em 3 e entregando 6 números: 3, 4, 5, 6, 7, 8

ATENÇÃO: ***Como no exemplo anterior, o último número entregue sempre será anterior ao parâmetro de limite (no caso o 9).***

## Sequencia com início, fim e passo:

range(2,10,2) vai retornar um enumerador iniciando em 2, terminando em 10, e com passo de 2 elementos: 2, 4, 6, 8

# Exemplos

## Imprime números de 0 a 4
```python
for n in range(5):
    print(n)
```

```bash
0
1
2
3
4
```

## Imprime números de 1 a 4
```python
for n in range(1,5):
    print(n)
```

```bash
1
2
3
4
```

## Imprime números de 2 a 10 pulando 2
```python
for n in range(2,11,2):
    print(n)
```

```bash
2
4
6
8
10
```

## Imprime números de 100 a 1 pulando 10
```python
for n in range(100,1,-10):
    print(n, n*2)
```
```bash
100
90
80
70
60
50
40
30
20
10
```
