# Ex3.py
# Cazador de Listas: Dada la lista frutas = ["manzana", "banana", "pera"], pide al usuario un índice (número).
# Intenta imprimir la fruta en ese índice. Si el índice no existe, captura el IndexError y avisa al usuario.


frutas = ["manzana", "banana", "pera"]

try:
    num = int(input("Introduzca un índice (0, 1 o 2): "))
    print(f"Fruta: {frutas[num]}")
except IndexError:
    print("El indice no existe.")
except ValueError:
    print("¡Debes introducir un número entero!")
