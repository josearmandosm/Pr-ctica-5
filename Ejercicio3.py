from functools import reduce

# Ejercicio 3: Sumar dos listas elemento a elemento usando lambda

lista3_1 = [1, 2, 3]
lista3_2 = [4, 5, 6]

suma_listas = list(map(lambda x, y: x + y, lista3_1, lista3_2))

print(suma_listas)