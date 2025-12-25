"""
Cazador de Duplicados: Tienes esta lista con números repetidos: numeros = [1, 2, 2, 3, 4, 4, 5].
Conviértela en un set para eliminar los duplicados e imprime el resultado.
"""

numeros = [1, 2, 2, 3, 4, 4, 5]

nuevo_numeros = set(numeros)

print(*nuevo_numeros, sep=", ")

