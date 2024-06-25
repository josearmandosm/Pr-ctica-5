lista16 = [1, None, 2, None, 3, None, 4]

# Eliminar valores None usando filter y lambda
filtrada = list(filter(lambda x: x is not None, lista16))

print(filtrada)
