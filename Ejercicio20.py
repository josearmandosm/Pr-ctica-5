from functools import reduce

lista20_1 = [1, 2, 3]
lista20_2 = [4, 5, 6]

# Sumar los elementos de dos listas usando reduce y lambda
suma = reduce(lambda x, y: x + y, lista20_1 + lista20_2)

print(suma)
