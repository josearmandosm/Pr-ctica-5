lista15 = ['abc', 'def', 'ghi']

# Revertir cada palabra usando map y lambda
revertidas = list(map(lambda palabra: palabra[::-1], lista15))

print(revertidas)
