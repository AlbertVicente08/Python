"""
5. Calculadora de Área: Crea una función area_rectangulo(base, altura) que devuelva el área.
"""


def area_rectangul(base, altura):
    area = base * altura

    return f"el area es {area}"


base = int(input("Base: "))
altura = int(input("Altura: "))
print(area_rectangul(base, altura))
