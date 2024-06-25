from functools import reduce

# Ejercicio 6: Concatenar dos listas de listas usando lambda

lista6_1 = [[1, 2], [3, 4], [5, 6]]
lista6_2 = [['a', 'b'], ['c', 'd'], ['e', 'f']]

# Concatenar dos listas de listas usando lambda y reduce
concatenadas = reduce(lambda acc, x: acc + x, lista6_1 + lista6_2, [])

print(concatenadas)
