## Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.

import random

lista = []

for i in range(10):
    lista.append(random.randint(1, 100))

for num in lista:
    if num % 3 == 0:
        print(num)