from functools import reduce

# Ejercicio 2: Filtrar números pares de una lista usando filter y lambda

lista2 = [10, 11, 12, 13, 14]

numeros_pares = list(filter(lambda x: x % 2 == 0, lista2))

print(numeros_pares)