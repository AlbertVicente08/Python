"""
El Bucle for (Para cada...)
Se usa cuando sabemos cuántas veces queremos repetir algo o cuando queremos recorrer una colección.
"""

# 1. Recorriendo una lista
nombres = ["Ana", "Beto", "Carla"]
for persona in nombres:
    print(f"Hola, {persona}")

# 2. Repitiendo un número fijo de veces (range)
# range(5) genera los números 0, 1, 2, 3, 4
for i in range(5):
    print(f"Repetición número {i}")
