---
title: Python - Calculadora V2
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


OPERACOES = {
    '+': lambda n1, n2: n1+n2,
    '-': lambda n1, n2: n1-n2,
    '*': lambda n1, n2: n1*n2,
    '/': lambda n1, n2: n1/n2,
    '**': lambda n1, n2: n1**n2
}


n1 = input_numero('Número 1 ')
n2 = input_numero('Número 2 ')
operacao = input(f'Operação ({list(OPERACOES.keys())}) ')
resultado = OPERACOES.get(
    operacao, lambda n1, n2: print('Operação inválida'))(n1, n2)
print(resultado)

```