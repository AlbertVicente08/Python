"""
9. Contador de Vocales: Crea una función contar_vocales(palabra) que reciba un texto y retorne cuántas vocales (a, e, i, o, u) contiene.
"""


def contar_vocales(palabra):
    contador = 0
    vocales = "aeiou"
    palabra_lower = palabra.lower()
    for letra in palabra_lower:
        if letra in vocales:
            contador += 1
    return contador


palabra = input("Introduce una palabra: ")
print(f"Hay un total de {contar_vocales(palabra)} vocales")
