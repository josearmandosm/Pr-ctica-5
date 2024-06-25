def km_a_millas(km):
    return km * 0.621371

lista13 = [10, 20, 30, 40, 50]

# Convertir lista de kilómetros a millas usando map y lambda
millas_list = list(map(lambda x: km_a_millas(x), lista13))

print(millas_list)
