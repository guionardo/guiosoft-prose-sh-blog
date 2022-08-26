---
title: Python - Indentação
description: Indentação
date: 2022-08-25
tags: [indent]
---
[Início](python-curso)

Os blocos de código são indentados à direita, com 2 ou 4 espaços a partir do código dono do contexto.

No exemplo abaixo, os comandos _if_, _elif_ e _else_ são os donos dos blocos imediatamente aninhados com a indentação na sua sequencia.

Observem que o último caractere dos comandos "donos" de blocos de código terminam sempre com *:* (dois pontos).

```python
'''
INDENTAÇÂO
'''

# Exemplo com if/elif/else
idade = 18

if idade > 60:      # Dono do bloco aninhado abaixo
    print('Idoso')  # Bloco de código
elif idade >= 30:   # Dono do bloco aninhado abaixo
    print('Adulto') # Bloco de código
elif idade >= 18:   # Dono do bloco aninhado abaixo
    print('Jovem')  # Bloco de código
elif idade >= 12:
    print('Adolescente')
    print('OI')
    print('AI')
elif idade > 1:
    print('Criança')
else:
    print('Bebe')

# Exemplo de função
def funcao(argumento):  # Dono do bloco aninhado abaixo
    print('Argumento', argumento)

# Exemplo de loop
for num in range(10):   # Dono do bloco aninhado abaixo
    print('Número', num)
```