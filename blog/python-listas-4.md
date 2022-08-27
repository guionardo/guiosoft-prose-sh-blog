# Números aleatórios, listas, contém e não-contém

```python
from random import randint

# Criar uma lista de 100 números aleatórios

lista_rand = [randint(1, 100)
              for _ in range(100)]

print('LISTA_RAND', lista_rand)

# Obter uma lista de números únicos a partir
# da lista_rand

lista_unicos = list(set(lista_rand))
print('LISTA_UNICOS', lista_unicos)

# Obter os números de 1 a 100 que não estão
# na lista_rand

lista_faltantes = []
for numero in range(1, 101):
    if numero not in lista_rand:
        lista_faltantes.append(numero)

print('LISTA_FALTANTES', lista_faltantes)
```
