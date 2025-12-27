# Ex4.py
# Diccionario Seguro: Dado el diccionario colores = {"rojo": "#FF0000", "verde": "#00FF00"},
# intenta acceder a una clave que no existe (ej: "azul") dentro de un bloque try/except para capturar el KeyError.

colores = {"rojo": "#FF0000", "verde": "#00FF00"}

try:
    intento = input("Introduzca el color que desea (rojo/verde): ").lower()
    print(f"El código hexadecimal de {intento} es: {colores[intento]}")

except KeyError:
    print(f"Error: El color '{intento}' no está en el diccionario.")
