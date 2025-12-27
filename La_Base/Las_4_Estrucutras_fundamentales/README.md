# Las 4 Estructuras Fundamentales de Python

En este módulo exploro las diferentes formas en las que Python puede agrupar y organizar colecciones de datos.

---

## 📚 Teoría

### 1. Listas (`[]`)

Son colecciones **ordenadas y mutables** (modificables). Son como una mochila donde metes cosas en un orden específico y puedes cambiarlas después.

```python
frutas = ["Manzana", "Banana", "Cereza"]
frutas.append("Uva")      # Agrega al final
frutas[1] = "Fresa"       # Modifica un elemento
```

### 2. Tuplas (`()`)

Son colecciones **ordenadas pero inmutables**. Una vez creadas, no se pueden cambiar. Son como una lista "grabada en piedra".

```python
coordenadas = (10, 20)
# coordenadas[0] = 50  # ¡ERROR! No se puede modificar
```

### 3. Conjuntos / Sets (`{}`)

Son colecciones **desordenadas de elementos únicos**. No permiten duplicados. Ideales para eliminar repeticiones.

```python
colores = {"Rojo", "Verde", "Azul", "Rojo"}
print(colores) # Salida: {'Azul', 'Rojo', 'Verde'} (el duplicado desaparece)
```

### 4. Diccionarios (`{clave: valor}`)

Almacenan datos en pares **Clave: Valor**. Buscas por una clave única en lugar de una posición.

```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}
print(persona["nombre"])  # Salida: Ana
```

---

## 📝 Retos y Ejercicios (`/Ejercicios`)

He completado los siguientes 10 ejercicios de manipulación de estructuras:

1. **[Ex1](./Ejercicios/Ex1.py)**: Mi Primera Lista (Creación e impresión limpia).
2. **[Ex2](./Ejercicios/Ex2.py)**: El Elegido (Acceso por índice).
3. **[Ex3](./Ejercicios/Ex3.py)**: Actualización de Inventario (Uso de `.append()`).
4. **[Ex4](./Ejercicios/Ex4.py)**: Tupla Intocable (Concepto de inmutabilidad).
5. **[Ex5](./Ejercicios/Ex5.py)**: Diccionario Básico (Estructura Clave:Valor).
6. **[Ex6](./Ejercicios/Ex6.py)**: Cazador de Duplicados (Conversión a `set`).
7. **[Ex7](./Ejercicios/Ex7.py)**: Agenda Inteligente (Modificación de diccionarios).
8. **[Ex8](./Ejercicios/Ex8.py)**: Mezclando Estructuras (Listas de Diccionarios / Nesting).
9. **[Ex9](./Ejercicios/Ex9.py)**: Suma de Lista (Uso de la función `sum()`).
10. **[Ex10](./Ejercicios/Ex10.py)**: El Último de la Fila (Índices negativos `[-1]`).

## 💡 Conceptos Clave Aprendidos

- **Mutable vs Inmutable**: Diferencia crítica entre Listas y Tuplas.
- **Unpacking (`*`)**: Técnica para limpiar la salida en consola.
- **Nesting**: Anidación de estructuras (ej: diccionarios dentro de listas).
- **Sets**: Limpieza automática de datos repetidos.
