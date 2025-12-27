# Ex9.py
# Validar Edad (Raise): Crea una función verificar_edad(edad).
# Si la edad es negativa, usa raise ValueError con el mensaje "Edad imposible".
# Luego, fuera de la función, usa un bloque try/except para capturar ese error específico.


def verificar_edad(edad):
    if edad < 0:
        raise ValueError("Edad imposible")
    else:
        print(f"La edad es de {edad}")


# --- PARTE FUERA DE LA FUNCIÓN ---
try:
    user_input = input("Que edad tienes: ")
    edad = int(user_input)  # Esto también podría dar ValueError si no es un número
    verificar_edad(edad)  # Aquí es donde capturamos el error que lanza la función
except ValueError as e:
    # Si la edad es negativa, imprimirá: Error Capturado: Edad imposible
    print(f"Error Capturado: {e}")
