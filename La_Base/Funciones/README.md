# Módulo 4: Funciones en Python ⚙️

En este módulo se explora el concepto de **Funciones**, bloques de código reutilizables diseñados para realizar tareas específicas.

---

## 📚 Teoría

### 1. ¿Qué es una Función?

Una función es un bloque de código con nombre que realiza una tarea y puede ser reutilizado.

- **Entrada (Parámetros):** Ingredientes.
- **Proceso (Cuerpo):** Preparación.
- **Salida (Return):** Resultado final.

### 2. Definición y Llamada

```python
# Definición
def saludar():
    print("¡Hola!")

# Llamada
saludar()
```

### 3. Parámetros y Argumentos

```python
def saludar_persona(nombre): # 'nombre' es el parámetro
    print(f"Hola, {nombre}")

saludar_persona("Ana") # "Ana" es el argumento
```

### 4. `return` vs `print`

- **`print`**: Solo muestra el dato en pantalla.
- **`return`**: Devuelve el dato para que el programa pueda guardarlo y usarlo después.

```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3) # Guardamos el valor devuelto
```

### 5. Parámetros por Defecto

```python
def preparar_cafe(tipo="Americano"):
    print(f"Sirviendo un café {tipo}")

preparar_cafe() # Usa el valor por defecto "Americano"
```

---

## 📝 Ejercicios Prácticos (`/Ejercicios`)

Se han completado 10 ejercicios que cubren la modularidad:

1.  **Ex1.py**: Saludo simple ("¡Hola Python!").
2.  **Ex2.py**: Bienvenida personalizada con retorno de string.
3.  **Ex3.py**: Cálculo del cuadrado de un número.
4.  **Ex4.py**: Convertidor de años a días vividos.
5.  **Ex5.py**: Calculadora de área de un rectángulo.
6.  **Ex6.py**: Verificador de números pares (retorno booleano).
7.  **Ex7.py**: Comparador de dos números (el mayor).
8.  **Ex8.py**: Calculadora de descuentos con parámetros por defecto.
9.  **Ex9.py**: Contador de vocales en una frase.
10. **Ex10.py**: Cálculo del promedio de una lista.

## 💡 Conceptos Clave

- **DRY (Don't Repeat Yourself)**: Evitar la duplicación de código.
- **Modularidad**: Dividir el programa en piezas pequeñas y manejables.
- **Scope (Alcance)**: Variables locales vs globales.
