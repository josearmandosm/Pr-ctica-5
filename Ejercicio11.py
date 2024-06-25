def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

lista11 = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números primos usando filter y lambda
numeros_primos = list(filter(lambda x: es_primo(x), lista11))

print(numeros_primos)
