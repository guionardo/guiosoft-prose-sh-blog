---
title: Python - Ex 99 - Escolha do Usuário
description: Exercício
date: 2022-09-06
tags: [print,while,for]
---
[Início](python-curso)


Dado um dicionário com chaves e valores, mostre as chaves ao usuário, e peça que ele escolha uma das chaves. Ao receber uma chave inexistente, refaça a pergunta. Ao final, apresente o valor da chave pedida.

```python
def escolha(opcoes):
  while True:
    for chave,valor in opcoes.items():
      print(chave,'=',valor)
    opcao = input('Escolha: ')
    if opcao in opcoes:
      return opcoes[opcao]

OPCOES = {
    'b':'banana',
    'l':'laranja',
    'c':'caqui',
    'u':'uva'
}

opcao = escolha(OPCOES)
print(opcao)
```