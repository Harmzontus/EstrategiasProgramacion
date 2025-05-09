def mochilaMemo(valores, pesos, capacidad):
    n = len(valores)
    memo = {}

    def dp(i, w):
        # Caso base: no hay objetos o no hay capacidad
        if i == 0 or w == 0:
            return 0

        # Verificamos si ya está resuelto
        if (i, w) in memo:
            return memo[(i, w)]

        if pesos[i - 1] > w:
            # No se puede incluir el objeto i-1 (peso excesivo)
            resultado = dp(i - 1, w)
        else:
            # Elegimos el mejor entre incluirlo o no
            include = valores[i - 1] + dp(i - 1, w - pesos[i - 1])
            exclude = dp(i - 1, w)
            resultado = max(include, exclude)

        memo[(i, w)] = resultado
        return resultado

    max_value = dp(n, capacidad)
    return max_value

# Datos del problema
valores = [2, 5, 10, 14, 15]     # valores de A, B, C, D, E
pesos = [1, 3, 4, 5, 7]       # pesos de A, B, C, D, E
capacidad = 8                   # capacidad de la mochila

# Ejecutar
resultado = mochilaMemo(valores, pesos, capacidad)
print(f"Valor maximo que se puede obtener: {resultado}")
