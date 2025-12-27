"""
Buscador de Tesoros (for + if): Tienes cofre = ["Piedra", "Papel", "Oro", "Arena"].
Recorre la lista con un for.
Si el elemento es "Oro", imprime "¡Encontrado!" y deten el bucle con break.
"""

cofre = ["Piedra", "Papel", "Oro", "Arena"]

for objeto in cofre: # Recorremos cada cosa que haya en el cofre, sin importar cuántas sean
    if objeto == "Oro":
        print("¡Encontrado!")
        break # Detenemos el bucle inmediatamente