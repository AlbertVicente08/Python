# 1. El Palíndromo Flexible
# El Reto: Crea una función que detecte si una frase es un palíndromo (se lee igual al revés), pero ignorando espacios y mayúsculas.
# Input: "Anita lava la tina"
# Output: True
# Por qué sirve: Tienes que limpiar el string (quitar espacios, pasar a minúsculas) y luego usar la lógica de inversión ([::-1])


def limpiar_cadena(cadena):
    eliminar_espacio = " "

    cadena_sin_espacio = cadena.replace(eliminar_espacio, "")
    cadena_sin_mayus = cadena_sin_espacio.lower()
    invertido(cadena_sin_mayus)


def invertido(cadena_limpia):
    cadena_invertida = cadena_limpia[::-1]
    comparar(cadena_limpia, cadena_invertida)


def comparar(normal, invertido):
    print(f"Normal: {normal}")
    print(f"Invertido: {invertido}")
    if normal == invertido:
        print("Es polindromo")
    else:
        print("No es polindromo")

def main():
    frase = input("Escribe algo: ")
    limpiar_cadena(frase)


main()
