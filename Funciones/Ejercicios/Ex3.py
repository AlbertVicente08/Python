"""
3. Cuadrado de un número: Crea una función cuadrado(n) que tome un número y retorne ese número elevado al cuadrado.
"""


def cuadrado(n):
    resultado = n**2
    return resultado


num = int(input("Tu numero: "))
print(cuadrado(num))
