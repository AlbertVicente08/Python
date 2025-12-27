"""
Son colecciones ordenadas y mutables (modificables). 
Son como una lista de compras o una lista de tareas: puedes agregar cosas, quitarlas y cambiar el orden.
Sintaxis: Corchetes [].
Analogía: Una mochila donde metes cosas en un orden específico.

"""

# Creación de una lista
frutas = ["Manzana", "Banana", "Cereza"]

# Acceso (por posición, empezando en 0)
print(frutas[0])  # Salida: Manzana

# Modificación
frutas.append("Uva")      # Agrega al final
frutas[1] = "Fresa"       # Cambia "Banana" por "Fresa"
