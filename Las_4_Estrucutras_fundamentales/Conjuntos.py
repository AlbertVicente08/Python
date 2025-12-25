"""
Son colecciones desordenadas de elementos únicos. No permiten duplicados. 
Son ideales para eliminar repeticiones o hacer operaciones matemáticas de conjuntos (unión, intersección).

Sintaxis: Llaves {} (pero sin dos puntos dentro).

Analogía: Una bolsa de canicas de colores. No importa el orden en que las saques, y si intentas meter una canica roja cuando ya hay una, la bolsa la rechaza.

"""

# Creación (fíjate que "Rojo" está repetido)
colores = {"Rojo", "Verde", "Azul", "Rojo"}

print(colores)
# Salida posible: {'Azul', 'Rojo', 'Verde'} 
# (El orden varía y el "Rojo" duplicado desapareció)