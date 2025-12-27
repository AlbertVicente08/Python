"""
8. Calculadora de Descuentos: Crea una función precio_final(precio, descuento=10) (con descuento por defecto del 10%).
Debe retornar el precio restando el porcentaje de descuento.
"""


def precio_final(precio, descuento=10):
    p_final = precio - (precio * descuento / 100)
    return p_final


precio = int(input("Precio: "))
print(precio_final(precio))
