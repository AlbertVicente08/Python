# Ex5.py
# Calculadora Robusta: Crea una función que pida dos números al usuario y los sume.
# Debe manejar dos errores posibles: que el usuario no escriba números (ValueError)
# y cualquier otro error inesperado (Exception).

def calc_rob():
    try:
        a = int(input("Escribe el numero (a): "))
        b = int(input("Escribe el numero (b): "))
        c = a + b
        print(f"El resultado es {c}")
    except ValueError:
        print("Error: ¡Debes escribir números!")
    except Exception as e: 
        print(f"Error inesperado: {e}")

calc_rob()