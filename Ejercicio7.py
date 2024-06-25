# Ejercicio 7: Sumar todos los elementos de una lista usando reduce y lambda

from functools import reduce

lista7 = [1, 2, 3, 4, 5]

suma_total = reduce(lambda x, y: x + y, lista7)

print(suma_total)
