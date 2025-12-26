"""
7. El Mayor de Dos: Crea una función mayor(a, b) que reciba dos números y retorne el más grande de los dos. Si son iguales, que retorne cualquiera.
"""


def mayor(a, b):
    if a > b:
        return f"El numero {a} es mayor (a)"
    elif b > a:
        return f"El numero {b} es mayor (b)"
    else:
        return "Son iguales"


a = int(input("Tu numero (a): "))
b = int(input("Tu numero (b): "))
print(mayor(a, b))
