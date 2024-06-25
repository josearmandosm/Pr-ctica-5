from functools import reduce

# Ejercicio 5: Unir dos listas de strings usando zip

lista5_1 = ['a', 'b', 'c']
lista5_2 = ['x', 'y', 'z']

union_listas = [x + y for x, y in zip(lista5_1, lista5_2)]

print(union_listas)
