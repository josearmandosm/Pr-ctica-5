from functools import reduce

lista8 = [2, 3, 4, 5]

# Multiplicar todos los elementos de la lista usando reduce y lambda
producto_total = reduce(lambda x, y: x * y, lista8)

print(producto_total)
