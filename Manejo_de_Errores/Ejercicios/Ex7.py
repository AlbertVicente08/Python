# Ex7.py
# Limpieza con Finally: Simula una conexión. Imprime "Abriendo conexión..." dentro del try.
# Provoca un error a propósito (ej: 1/0). Usa finally para imprimir "Cerrando conexión...",
# asegurándote de que se imprima aunque haya error.


try:
    print("Abriendo conexion...")
    print(1 / 0)
except ZeroDivisionError:
    print("error")
finally:
    print("Cerrando conexion")