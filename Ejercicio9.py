from functools import reduce

lista9 = [10, 2, 30, 4, 50]

# Encontrar el máximo de la lista usando reduce y lambda
maximo = reduce(lambda x, y: x if x > y else y, lista9)

print(maximo)
