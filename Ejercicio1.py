from functools import reduce

# Ejercicio 1: Elevar al cuadrado cada elemento de una lista usando map y lambda

lista1 = [1, 2, 3, 4, 5]

lista_cuadrados = list(map(lambda x: x**2, lista1))

print(lista_cuadrados)
