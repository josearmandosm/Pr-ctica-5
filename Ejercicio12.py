def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

lista12 = [0, 10, 20, 30, 40]

# Convertir lista de Celsius a Fahrenheit usando map y lambda
fahrenheit_list = list(map(lambda x: celsius_a_fahrenheit(x), lista12))

print(fahrenheit_list)
