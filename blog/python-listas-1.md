---
title: Python - Listas 01
description: Operações com listas
date: 2022-08-25
tags: [list,set]
---
[Início](python-curso)
```python
# Criar uma lista de nomes
nomes = ['Zé', 'Maria', 'André']

# Adicionar nomes à lista
nomes.append('João')
nomes.append('Zé')

# Imprimir quantos 'Zé' existem na lista
print(nomes.count('Zé'))

# Extender a lista com os items de outra lista
nomes.extend(['Juca', 'Ben'])

# Obter um set de nomes (o set não aceita itens duplicados)
unicos = set(nomes)

# Imprimir as variáveis
print(nomes)
print(unicos)
```