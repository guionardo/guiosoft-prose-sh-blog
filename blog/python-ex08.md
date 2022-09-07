---
title: Python - Ex 08 - Data nascimento
description: Exercício
date: 2022-09-06
tags: [set,input,int,if,not]
---
[Início](python-curso)


Faça um programa que receba uma data de nascimento (15/07/87) e imprima 'Você nasceu em <dia> de <mês> de <ano>'

```python
texto = input('Informe data de nascimento (dd/mm/aa)')

dia = int(texto[0:2])
if not (1 <= dia <= 31):
  print('DIA INVÁLIDO')
  exit()

mes = int(texto[3:5])
if not (1 <= mes <= 12):
  print('MÊS INVÁLIDO')
  exit()

ano = int(texto[6:8])
if not (0 <= ano <= 99):
  print('ANO INVÁLIDO')
  exit()

MESES = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

print('Você nasceu em ',dia,' de ',MESES[mes],' de ',ano)
```