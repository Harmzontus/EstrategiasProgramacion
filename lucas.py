def lucas_tab(n):
    # Caso base: si n es 0, el valor es 2 (Lucas(0) = 2)
    if n == 0:
        return 2
    # Caso base: si n es 1, el valor es 1 (Lucas(1) = 1)
    if n == 1:
        return 1

    # Inicializamos una lista para almacenar los resultados de la secuencia de Lucas hasta el n-ésimo término
    lucas = [0] * (n + 1)  # Lista con n+1 elementos, inicialmente todos 0
    lucas[0] = 2  # Lucas(0) = 2
    lucas[1] = 1  # Lucas(1) = 1

    # Iteramos desde el índice 2 hasta n para calcular los siguientes valores de la secuencia
    for i in range(2, n + 1):
        lucas[i] = lucas[i - 1] + lucas[i - 2]  # La fórmula de la secuencia de Lucas: L(n) = L(n-1) + L(n-2)

    # Devolvemos el valor en el índice n de la lista
    return lucas[n]

# Función de la secuencia de Lucas usando memorización (recursión con almacenamiento de resultados previos)
def lucas_memo(n, memo=None):
    if memo is None:
        memo = {}  # Inicializamos el diccionario de memoización si es la primera vez

    # Si ya hemos calculado el valor para n, lo devolvemos directamente
    if n in memo:
        return memo[n]

    # Caso base: si n es 0, el valor es 2 (Lucas(0) = 2)
    if n == 0:
        return 2
    # Caso base: si n es 1, el valor es 1 (Lucas(1) = 1)
    if n == 1:
        return 1

    # Calculamos Lucas(n) y almacenamos el resultado en memo para evitar cálculos repetidos
    memo[n] = lucas_memo(n - 1, memo) + lucas_memo(n - 2, memo)
    return memo[n]  # Devolvemos el valor calculado de Lucas(n)

# Bucle para imprimir los primeros 10 términos de la secuencia de Lucas usando memorización
for i in range(10):
    # Usamos la versión con memorización y mostramos el resultado para cada valor de i
    print(f"Lucas({i}) - Memorizacion: {lucas_memo(i)}")
