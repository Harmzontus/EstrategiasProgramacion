def construir_tabla_binomial(n):
    # Creamos una tabla bidimensional (matriz) con (n+1) filas y (n+1) columnas
    tabla = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # Recorremos cada fila desde 0 hasta n
    for i in range(n + 1):
        # Cada fila tiene de 0 a i columnas válidas
        for k in range(i + 1):
            # Caso base: si k == 0 o k == i, el valor es 1
            if k == 0 or k == i:
                tabla[i][k] = 1
            else:
                # Usamos la fórmula recursiva del triángulo de Pascal
                tabla[i][k] = tabla[i-1][k-1] + tabla[i-1][k]

    return tabla

# Función para obtener un coeficiente específico usando la tabla
def coef_binomial(n, k):
    tabla = construir_tabla_binomial(n)
    return tabla[n][k]

# Ejemplo de uso
n = 6
k = 2
print(f"Coeficiente binomial C({n}, {k}) = {coef_binomial(n, k)}")


def imprimir_tabla_binomial(n):
    tabla = construir_tabla_binomial(n)

    print(f"Triangulo de Pascal hasta fila {n}:\n")
    for i in range(n + 1):
        # Imprimir espacios para dar forma triangular
        print(" " * (n - i) * 2, end="")

        # Imprimir valores de la fila
        for k in range(i + 1):
            print(f"{tabla[i][k]:4}", end=" ")  # Formato ancho para alinear columnas
        print()  # Salto de línea al final de cada fila

# Llamar a la función para mostrar la tabla hasta la fila 6 
imprimir_tabla_binomial(6)