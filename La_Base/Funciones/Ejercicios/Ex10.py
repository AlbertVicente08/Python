"""
10. Promedio de una Lista: Crea una función calcular_promedio(lista_numeros) que reciba una lista de números (ej: [10, 20, 30]) y devuelva el promedio aritmético.
"""


def calcular_promedio(lista_numeros):
    cantidad = len(lista_numeros)
    suma = sum(lista_numeros)
    promedio = suma / cantidad
    return promedio


lista = [10, 20, 30]
print(f"El promedio es {calcular_promedio(lista)}")
