# Ex8.py
# Validador de Tipos: Crea una función sumar_lista(lista) que sume todos los elementos.
# Si la lista contiene algo que no sea un número (ej: [1, 2, "a"]),
# captura el TypeError e imprime "La lista contiene elementos no numéricos".


def sumar_lista(lista):
    try:
        return sum(lista)
    except TypeError:
        print("La lista contiene elementos no numericos")


numeros = [5, 32, 7]
print(sumar_lista(numeros))
