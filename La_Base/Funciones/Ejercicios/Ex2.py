"""
2. Bienvenida Personalizada: Crea una función bienvenida(nombre) que reciba un nombre y devuelva (return) el string "Bienvenido a Python, [nombre]". Luego imprime el resultado.
"""


def bienvenida(nombre):
    return f"Bienvenido a python {nombre}"


nombre = input("Tu nombre: ")
print(bienvenida(nombre))
