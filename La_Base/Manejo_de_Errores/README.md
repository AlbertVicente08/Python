# Manejo de Errores en Python

## 1. ¿Qué es una Excepción?

Imagina que estás conduciendo.

- **Código normal:** Conduces por la carretera sin problemas.
- **Error (Excepción):** De repente, hay un bache gigante.
- **Sin manejo de errores:** El coche se rompe y te quedas tirado (el programa se detiene/crashea).
- **Con manejo de errores:** Tienes amortiguadores de lujo. Sientes el bache, pero el coche sigue avanzando.

En Python, usamos los bloques `try` y `except` para construir esos "amortiguadores".

---

## 2. La Estructura Fundamental

### A. El bloque básico `try` / `except`

Intentamos ejecutar un código peligroso. Si falla, Python salta inmediatamente al bloque `except` en lugar de detener el programa.

```python
try:
    # Código que podría fallar
    numero = int(input("Introduce un número: "))
    print(f"Tu número es {numero}")
except:
    # Código que se ejecuta SI hay un error arriba
    print("¡Eso no es un número válido!")

print("El programa continúa...") # Esto se imprime pase lo que pase
```

### B. Capturando errores específicos

No todos los errores son iguales. Es mejor saber qué falló.

- **ZeroDivisionError:** Dividir por cero.
- **ValueError:** Tipo de dato incorrecto (ej: intentar convertir "hola" a entero).
- **IndexError:** Buscar una posición que no existe en una lista.

```python
try:
    dividendo = 10
    divisor = 0
    resultado = dividendo / divisor
except ZeroDivisionError:
    print("¡Error! No puedes dividir por cero.")
except ValueError:
    print("Error de valor.")
```

### C. La familia completa: `else` y `finally`

- **else:** Se ejecuta si NO hubo ningún error en el `try`.
- **finally:** Se ejecuta SIEMPRE, haya error o no (ideal para limpiezas, cerrar archivos, bases de datos, etc.).

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Falló la división")
else:
    print(f"Todo salió bien, el resultado es {x}")
finally:
    print("Operación finalizada (esto sale siempre).")
```

### D. Lanzar tus propios errores (`raise`)

A veces tú quieres provocar el error si algo no cumple tus reglas.

```python
def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return edad

try:
    verificar_edad(-5)
except ValueError as e:
    print(f"Error capturado: {e}")
```

---

## ✅ Ejercicios Prácticos (`/Ejercicios`)

Aquí tienes 10 ejercicios para dominar el manejo de excepciones:

1.  **[Ex1.py](./Ejercicios/Ex1.py)**: ✅ División Segura (`ZeroDivisionError`).
2.  **[Ex2.py](./Ejercicios/Ex2.py)**: ✅ Conversión de Enteros (`ValueError`).
3.  **[Ex3.py](./Ejercicios/Ex3.py)**: ✅ Cazador de Listas (`IndexError`).
4.  **[Ex4.py](./Ejercicios/Ex4.py)**: ✅ Diccionario Seguro (`KeyError`).
5.  **[Ex5.py](./Ejercicios/Ex5.py)**: ✅ Calculadora Robusta (Múltiples errores).
6.  **[Ex6.py](./Ejercicios/Ex6.py)**: ✅ El Bloque `else` (Flujo de éxito).
7.  **[Ex7.py](./Ejercicios/Ex7.py)**: ✅ Limpieza con `finally` (Limpieza obligatoria).
8.  **[Ex8.py](./Ejercicios/Ex8.py)**: ✅ Validador de Tipos (`TypeError`).
9.  **[Ex9.py](./Ejercicios/Ex9.py)**: ✅ Validar Edad (`raise`).
10. **[Ex10.py](./Ejercicios/Ex10.py)**: ✅ Bucle de Insistencia (Patrón `while True`).

---

_¡Módulo completado con éxito!_
