"""
Esta es quizás la estructura más poderosa. Almacenan datos en pares Clave: Valor. 
En lugar de buscar por posición (índice 0, 1...), buscas por una "clave" única.

Sintaxis: Llaves {} con pares clave: valor.

Analogía: Un diccionario real o una agenda telefónica. Buscas "Juan" (clave) para obtener su "Número" (valor).
"""

# Creación
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceso
print(persona["nombre"])  # Salida: Ana

# Modificación
persona["profesion"] = "Ingeniera"  # Agrega una nueva clave


