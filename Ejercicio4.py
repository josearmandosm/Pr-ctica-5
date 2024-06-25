from functools import reduce

# Ejercicio 4: Multiplicar dos listas elemento a elemento usando zip

lista4_1 = [2, 3, 4]
lista4_2 = [5, 6, 7]

producto_listas = [x * y for x, y in zip(lista4_1, lista4_2)]

print(producto_listas)