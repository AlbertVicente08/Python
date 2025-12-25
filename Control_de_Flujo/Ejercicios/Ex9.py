"""
Tabla de Multiplicar (for): Define numero = 7.
Usa un for del 1 al 10 para imprimir la tabla completa: "7 x 1 = 7", "7 x 2 = 14", etc.
"""

numero = 7

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
