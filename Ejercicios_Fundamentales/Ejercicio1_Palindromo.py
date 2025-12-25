# 1. El Palíndromo Flexible
# El Reto: Crea una función que detecte si una frase es un palíndromo (se lee igual al revés), pero ignorando espacios y mayúsculas.
# Input: "Anita lava la tina"
# Output: True
# Por qué sirve: Tienes que limpiar el string (quitar espacios, pasar a minúsculas) y luego usar la lógica de inversión ([::-1])



import unicodedata  # Importamos la herramienta para manejar caracteres especiales

def normalizar_texto(cadena):
    
    """
    1. Convierte a minúsculas.
    2. Separa las tildes de las letras (Descomposición NFD).
    3. Elimina los signos de puntuación y tildes, dejando solo letras base y números.
    """
    # Paso A: Pasamos a minúsculas
    texto = cadena.lower()
    
    # Paso B: Separamos letras de tildes (ej: 'á' se convierte en 'a' + '´')
    texto_descompuesto = unicodedata.normalize('NFD', texto)
    
    # Paso C: Filtramos. 
    # unicodedata.category(c) != 'Mn' significa: "Si NO es una marca (tilde), guárdalo".
    # isalnum() asegura que tampoco pasen comas o puntos.
    texto_limpio = ""
    for i in texto_descompuesto:
        if unicodedata.category(i) != 'Mn' and i.isalnum():
            texto_limpio += i
    return texto_limpio

def es_palindromo(cadena):
    """
    Verifica si la cadena es palíndromo ignorando tildes, mayúsculas y signos.
    """
    texto_procesado = normalizar_texto(cadena)
    return texto_procesado == texto_procesado[::-1]

def main():
    print("--- DETECTOR DE PALÍNDROMOS DEFINITIVO ---")
    frase = input("Escribe una frase: ")
    
    if es_palindromo(frase):
        print(f"¡Es un palíndromo! ('{frase}')")
    else:
        print("No es un palíndromo.")

if __name__ == "__main__":
    main()