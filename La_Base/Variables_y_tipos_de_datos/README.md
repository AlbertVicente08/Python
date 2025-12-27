# Variables y Tipos de Datos

En este módulo aprendo los cimientos de Python: cómo guardar información y qué tipos de datos existen.

---

## 📚 Teoría

### 1. ¿Qué son las Variables?

Las variables son "etiquetas" que le ponemos a los datos para poder guardarlos en la memoria de la computadora y usarlos después.

```python
# Creando variables
mensaje = "Hola Mundo"  # Aquí la etiqueta es 'mensaje'
edad = 25               # Aquí la etiqueta es 'edad'
precio = 19.99          # Aquí la etiqueta es 'precio'
```

### 2. Tipos de Datos Fundamentales

- **Int (Enteros):** Números sin decimales.
  ```python
  vidas = 3
  anio = 2024
  ```
- **Float (Flotantes):** Números con parte decimal.
  ```python
  pi = 3.1416
  altura = 1.75
  ```
- **Str (Strings):** Texto o cadenas de caracteres.
  ```python
  nombre = "Guido van Rossum"
  numero_como_texto = "100"  # Es texto, no número matemático.
  ```
- **Bool (Booleanos):** Representan valores de verdad lógica: `True` o `False`.
  ```python
  es_de_dia = True
  esta_lloviendo = False
  ```

### 3. Conceptos Importantes

- **Tipado Dinámico:** No necesitas declarar el tipo de dato. Python lo deduce y puedes cambiarlo.
  ```python
  caja = 10        # Int
  caja = "Manzana" # Ahora es Str
  ```
- **Función `type()`:** Sirve para saber qué tipo de dato es una variable.
  ```python
  x = 9.5
  print(type(x))  # Salida: <class 'float'>
  ```

---

## 📝 Retos y Ejercicios (`/Ejercicios`)

He completado los siguientes 10 retos fundamentales:

1. **[Ex1](./Ejercicios/Ex1.py)**: Hola Variable (Strings básicos).
2. **[Ex2](./Ejercicios/Ex2.py)**: Identidad Secreta (Variables múltiples).
3. **[Ex3](./Ejercicios/Ex3.py)**: El Inspector (Uso de `type()`).
4. **[Ex4](./Ejercicios/Ex4.py)**: Matemáticas Simples (Operadores básicos).
5. **[Ex5](./Ejercicios/Ex5.py)**: Interruptor (Lógica booleana).
6. **[Ex6](./Ejercicios/Ex6.py)**: Concatenación (Unir textos).
7. **[Ex7](./Ejercicios/Ex7.py)**: Formateo de Cadenas (f-strings y decimales).
8. **[Ex8](./Ejercicios/Ex8.py)**: Conversión de Tipos (Casting).
9. **[Ex9](./Ejercicios/Ex9.py)**: Intercambio de Valores (Pythonic Swapping).
10. **[Ex10](./Ejercicios/Ex10.py)**: Calculadora de Área (Potencias `**` y Pi).

## 💡 Conceptos Clave Aprendidos

- **Snake Case**: Convención para nombrar variables (`mi_variable`).
- **Tipado Dinámico**: Python asigna tipos en tiempo de ejecución.
- **Operador `**`\*\*: Para potencias.
- **Casting**: `int()`, `float()`, `str()` para convertir datos.
