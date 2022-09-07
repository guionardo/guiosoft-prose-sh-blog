---
title: Python - Ex 07 - Vogais e frase
description: Exercício
date: 2022-09-06
tags: [set,input,lower,for,len]
---
[Início](python-curso)


Faça um programa que receba uma string e responda se ela tem alguma vogal. Se sim, quais são? E também diga se ela é uma frase ou não.

```python
texto = input('Digite algo: ')

vogais = set()
for letra in texto:
    if letra.lower() in 'aeiou':
        vogais.add(letra)

print('Vogais: ', vogais)

palavras = texto.split()
print('Palavras: ', palavras)

if len(palavras) > 1:
    print('É uma frase')
else:
    print('Não é uma frase')
```