---
title: Python - Calculadora
description: Calculadora
date: 2022-08-29
tags: [def]
---
[Início](python-curso)

## Funções e métodos

```python
def input_numero(pergunta='?'):
    while True:
        resposta = input(pergunta).strip()
        try:
            numero = float(resposta)
            return numero
        except:
            print('Número inválido')


def soma(n1, n2):
    return n1+n2


def subtracao(n1, n2):
    return n1-n2


def multiplicacao(n1, n2):
    return n1*n2


def divisao(n1, n2):
    return n1/n2


def potenciacao(n1, n2):
    return n1**n2


n1 = input_numero('Número 1')
n2 = input_numero('Número 2')

operacao = input('Operação (+,-,*,/) ')

if operacao == '+':
    resultado = soma(n1, n2)
elif operacao == '-':
    resultado = subtracao(n1, n2)
elif operacao == '*':
    resultado = multiplicacao(n1, n2)
elif operacao == '/':
    resultado = divisao(n1, n2)
elif operacao == '**':
    resultado = potenciacao(n1, n2)
else:
    print('Operação inválida')
    resultado = 0

print(resultado)
```