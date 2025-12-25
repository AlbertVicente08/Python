"""
El Bucle while (Mientras...)
Se usa cuando NO sabemos exactamente cuántas veces se repetirá el código,
pero sí sabemos la condición que debe cumplirse para seguir.
"""

bateria = 5

while bateria > 0:
    print(f"Batería restante: {bateria}%")
    bateria = (
        bateria - 1
    )  # Importante: modificar la condición para no crear un bucle infinito

print("¡Móvil apagado!")
