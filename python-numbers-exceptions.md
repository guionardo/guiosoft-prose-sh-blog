---
title: Python - Números e exceções
date: 2022-08-25
tags: [input,print,try,exception]
---
[Início](python-curso)

```python
## Perguntar números ao usuário e fazer operações com eles

```python
try:
    # Se o usuário informar um número inválido (espaço, letras, etc)
    # A exceção ValueError será lançada e capturada
    x = float(input('Numero 1: '))
    y = float(input('Numero 2: '))
    print(f'{x:.2f}+{y:.2f}={x+y:.2f}')
    print(f'{x}-{y}={x-y}')
    print(f'{x}*{y}={x*y}')

    # Se o usuário informar zero para o segundo número
    # A divisão por zero lançará a exceção ZeroDivisionError
    print(f'{x}/{y}={x/y}')

    print(f'{x}%{y}={x%y}')
    print(f'{x}//{y}={x//y}')
    print(f'{x}**{y}={x**y}')

except ZeroDivisionError:
    print("Não dá pra dividir por zero!")
except ValueError:
    print("O número deve ser válido!")
except Exception as exc:
    print('Erro geral', exc)
```