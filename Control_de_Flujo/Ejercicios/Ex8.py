"""
Validador de Contraseña (while + if): Define secreto = "python".
Usa un while para pedir al usuario una contraseña (usa input()).
Si acierta, imprime "Bienvenido" y rompe el bucle. Si falla, imprime "Intenta de nuevo".
"""

secreto = "python"

while True:
    contrasena = input("introduce la contrasena: ")
    if contrasena == secreto:
        print("Bienvenido")
        break
    else:
        print("Intentalo de nuevo")
        