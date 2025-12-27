# Ex6.py
# El Bloque Else: Escribe un código que intente convertir un string a número.
# Si funciona, usa el bloque else para imprimir "Conversión exitosa"
# y mostrar el número multiplicado por 2.
#


def string_a_numero(cadena):
    try:
        cadena_numero = int(cadena)
    except ValueError:
        print("Error")
    else:
        print("Conversion exitosa")
        print(cadena_numero * 3)


palabra = input("Escribe una cadena: ")
string_a_numero(palabra)
