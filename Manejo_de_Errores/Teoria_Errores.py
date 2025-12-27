# 1. ¿Qué es una Excepción?
# Imagina que estás conduciendo.
# Código normal: Conduces por la carretera sin problemas.
# Error (Excepción): De repente, hay un bache gigante.
# Sin manejo de errores: El coche se rompe y te quedas tirado (el programa se detiene/crashea).
# Con manejo de errores: Tienes amortiguadores de lujo. Sientes el bache, pero el coche sigue avanzando.
# En Python, usamos los bloques try y except para construir esos "amortiguadores".

# 2. La Estructura Fundamental

# A. El bloque básico try / except
# Intentamos ejecutar un código peligroso. Si falla, Python salta inmediatamente al bloque except en lugar de detener el programa.

try:
    # Código que podría fallar
    # numero = int(input("Introduce un número: "))
    numero = 10
    print(f"Tu número es {numero}")
except:  # noqa: E722
    # Código que se ejecuta SI hay un error arriba
    print("¡Eso no es un número válido!")

print("El programa continúa...")  # Esto se imprime pase lo que pase

# B. Capturando errores específicos
# No todos los errores son iguales. Es mejor saber qué falló.
# ZeroDivisionError: Dividir por cero.
# ValueError: Tipo de dato incorrecto (ej: intentar convertir "hola" a entero).
# IndexError: Buscar una posición que no existe en una lista.

try:
    dividendo = 10
    divisor = 0
    resultado = dividendo / divisor
except ZeroDivisionError:
    print("¡Error! No puedes dividir por cero.")
except ValueError:
    print("Error de valor.")

# C. La familia completa: else y finally
# else: Se ejecuta si NO hubo ningún error en el try.
# finally: Se ejecuta SIEMPRE, haya error o no (ideal para limpiezas, cerrar archivos, bases de datos, etc.).

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Falló la división")
else:
    print(f"Todo salió bien, el resultado es {x}")
finally:
    print("Operación finalizada (esto sale siempre).")

# D. Lanzar tus propios errores (raise)
# A veces tú quieres provocar el error si algo no cumple tus reglas.

try:
    edad = -5
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
except ValueError as e:
    print(f"Error capturado: {e}")
