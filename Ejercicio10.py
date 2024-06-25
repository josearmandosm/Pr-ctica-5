from functools import reduce

lista10 = [1, 2, 3, 4, 5]

# Calcular el promedio de la lista usando reduce y lambda
promedio = reduce(lambda x, y: x + y, lista10) / len(lista10)

print(promedio)
