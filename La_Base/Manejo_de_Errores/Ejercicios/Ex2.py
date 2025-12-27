# Ex2.py
# Conversión de Enteros: Pide al usuario que ingrese un número (usando input).
# Intenta convertirlo a entero (int()). Si el usuario escribe texto (ej: "hola"),
# captura el ValueError e imprime "Debes ingresar un número".


while True:    
    try:
        num = int(input("Ingresa un numero: "))
    except ValueError:
        print("Debes ingresar un numero")
    else:
        break
