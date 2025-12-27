# 🔀 Control de Flujo en Python

Este módulo cubre los conceptos esenciales para dirigir la ejecución de un programa en Python mediante condicionales y bucles.

---

## 📚 Teoría

### 1. Condicionales (`if`, `elif`, `else`)

Es la capacidad del programa para tomar decisiones. El código elige un camino dependiendo de si una condición es `True` o `False`.

```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### 2. Bucle `for` (Para cada...)

Se usa cuando sabemos cuántas veces queremos repetir algo o para recorrer una colección (listas, rangos, etc.).

```python
nombres = ["Ana", "Beto"]
for persona in nombres:
    print(f"Hola, {persona}")

# Repetir 5 veces
for i in range(5):
    print(i)
```

### 3. Bucle `while` (Mientras...)

Se usa cuando **no sabemos** cuántas veces se repetirá el código, pero sí la condición que debe cumplirse para seguir.

```python
bateria = 5
while bateria > 0:
    print(f"Batería: {bateria}%")
    bateria -= 1
```

---

## 🚀 Ejercicios Resueltos (`/Ejercicios`)

He completado una serie de 10 ejercicios prácticos:

1.  **[Ex1.py](./Ejercicios/Ex1.py)**: El Portero (Condicional simple).
2.  **[Ex2.py](./Ejercicios/Ex2.py)**: Contando Ovejas (Bucle `for` y `range`).
3.  **[Ex3.py](./Ejercicios/Ex3.py)**: Lista de la Compra (Iteración sobre listas).
4.  **[Ex4.py](./Ejercicios/Ex4.py)**: Cuenta Regresiva (Bucle `while`).
5.  **[Ex5.py](./Ejercicios/Ex5.py)**: Par o Impar (Operador módulo).
6.  **[Ex6.py](./Ejercicios/Ex6.py)**: Suma Total (Acumuladores).
7.  **[Ex7.py](./Ejercicios/Ex7.py)**: Buscador de Tesoros (`for` + `if` + `break`).
8.  **[Ex8.py](./Ejercicios/Ex8.py)**: Validador de Contraseña (`while` infinito).
9.  **[Ex9.py](./Ejercicios/Ex9.py)**: Tabla de Multiplicar (Formateo de strings).
10. **[Ex10.py](./Ejercicios/Ex10.py)**: FizzBuzz (Lógica compleja y divisibilidad).

## 💡 Conceptos Clave

- **Indentación**: Obligatoria en Python para definir bloques de código.
- **`range()`**: Genera una secuencia de números.
- **Control de Bucles**: `break` (salir) y `continue` (saltar a la siguiente iteración).
