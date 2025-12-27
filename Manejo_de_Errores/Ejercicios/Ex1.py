# Ex1.py
# División Segura: Crea una función dividir(a, b) que intente dividir a entre b.
# Si b es 0, debe capturar el error ZeroDivisionError e imprimir "No se puede dividir por cero", devolviendo None.


def dividir(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        return print("No se puede dividir entre cero")
    else:
        print(f"{c:.1f}")


a = int(input("Escribe el numero (a): "))
b = int(input("Escribe el numero (b): "))
dividir(a, b)
