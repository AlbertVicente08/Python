"""
Son colecciones ordenadas pero inmutables. 
Una vez creadas, no se pueden cambiar (no puedes agregar ni borrar nada). 
Se usan para datos que no deberían modificarse, como coordenadas GPS o días de la semana.

Sintaxis: Paréntesis ().

Analogía: Una lista grabada en piedra.
"""

# Creación
coordenadas = (10, 20)

# Acceso
print(coordenadas[0])  # Salida: 10

# coordenadas[0] = 50  # ¡ERROR! Python no te dejará hacer esto.