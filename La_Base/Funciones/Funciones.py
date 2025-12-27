"""
1. ¿Qué es una Función? (La Teoría)
Una función es un bloque de código que tiene un nombre, realiza una tarea específica
y puede ser reutilizado tantas veces como quieras.

La Analogía: La Licuadora
Imagina una licuadora:
Entrada (Parámetros): Le pones frutas y leche.
Proceso (Cuerpo de la función): Las cuchillas giran y mezclan todo.
Salida (Return): Te entrega un batido.

Sintaxis Básica
Para crear (definir) una función usamos la palabra clave def.
"""


def nombre_de_la_funcion(parametros):
    # Bloque de código (indentado)
    resultado = "valor"
    return resultado


"""
2. Conceptos Clave Paso a Paso
A. Definir y Llamar
Definir es "construir la máquina". Llamar es "usar la máquina".
"""


# 1. Definición
def saludar():
    print("¡Hola! Bienvenido a la clase.")


# 2. Llamada (Ejecución)
saludar()
saludar()  # Puedo usarla cuantas veces quiera

"""
B. Parámetros y Argumentos
Son los datos que la función necesita para trabajar (los ingredientes de la licuadora).
"""


# 'nombre' es el parámetro (la variable que espera recibir el dato)
def saludar_persona(nombre):
    print(f"Hola, {nombre}, ¡es un gusto verte!")


# 'Ana' es el argumento (el dato real que enviamos)
saludar_persona("Ana")
saludar_persona("Carlos")

"""
C. El vital return vs. print
Este es el concepto más importante para un principiante.
- print: Muestra algo en pantalla, pero el programa "olvida" el dato inmediatamente.
- return: Devuelve el dato para que el programa lo pueda guardar en una variable y usarlo después.
"""


def sumar(a, b):
    resultado = a + b
    return resultado  # Devuelve el valor, no lo imprime


# Guardo el resultado en una variable
total = sumar(5, 3)
print(f"El total es: {total}")

"""
D. Parámetros por defecto
Puedes dar valores iniciales por si el usuario no envía ninguno.
"""


def preparar_cafe(tipo="Americano"):
    print(f"Sirviendo un café {tipo}")


preparar_cafe("Cappuccino")  # Imprime: Sirviendo un café Cappuccino
preparar_cafe()  # Imprime: Sirviendo un café Americano (usa el default)
