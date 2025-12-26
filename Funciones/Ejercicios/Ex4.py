"""
4. Convertidor de Edad: Crea una función dias_vividos(anios) que reciba tu edad en años y devuelva la cantidad aproximada de días que has vivido (asume 365 días por año).
"""


def dias_vividos(anios):
    dias = anios * 365
    return f"has vivido un total de {dias} dias"


num = int(input("Tu numero: "))
print(dias_vividos(num))
