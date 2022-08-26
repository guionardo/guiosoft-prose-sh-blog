---
title: Python - loop enquanto
date: 2022-08-25
tags: [while, continue, break,input]
---
[Início](python-curso)

O comando *while* produz um laço de repetição que vai iterar enquanto uma condição estiver sendo válida, ou até ser interrompido explicitamente.

```python
while <condição booleana>:
    <comando1>
    <comando2>
    <comando...>
    <bloco de controle do loop>
```

De forma geral, enquanto a *condição booleana* for avaliada como True, o loop vai executar os comandos em sequencia e reiniciar indefinidamente.

Dentro do bloco de comandos dentro do while, é possível interromper o loop com o comando *break*.

Quando for necessário voltar ao início do loop, usa-se o comando *continue*.

## Exemplo

```python
# Perguntar um nome do usuário e repetir 
# indefinidamente caso não seja válido
while True: # Condição booleana, será sempre True
    nome = input('Nome?').strip()
    if not nome:
        # Se o usuário não informar o nome, o comando continue
        # mandará a execução para o início do while
        print('Você deve informar seu nome')
        continue
    if len(nome) < 2:
        # Se o usuário não informar um nome adequado
        # será enviado novamente para o início do while
        print('Você deve ter um nome com mais de 1 caracter')
        continue
    # Chegando nesse ponto, o nome do usuário estará válido
    # e o comando break vai interromper o loop do while
    break

print('Seu nome', nome)
```