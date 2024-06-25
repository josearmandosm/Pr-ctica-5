lista18 = [[1, 2], [3], [4, 5, 6], [7, 8]]

# Filtrar sublistas por longitud usando filter y lambda
filtradas = list(filter(lambda x: len(x) > 1, lista18))

print(filtradas)
