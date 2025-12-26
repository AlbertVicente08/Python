"""
6. ¿Es Par o Impar?: Crea una función es_par(numero) que devuelva True si el número es par y False si es impar. (Pista: usa el operador módulo %).
"""


def es_par(numero):
    return numero % 2 == 0


num = int(input("Tu numero: "))
print(es_par(num))
