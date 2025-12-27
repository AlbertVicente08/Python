"""
Par o Impar (if + Modulo): Pide un número (o defínelo en una variable).
Si el número dividido por 2 tiene resto 0 (num % 2 == 0), imprime "Par", si no, "Impar".
"""

n = int(input("Introduce un numero:"))

if n % 2 == 0:
    print("par")
else:
    print("impar")
