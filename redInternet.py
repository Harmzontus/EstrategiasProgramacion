import heapq

def prim(n, conexiones):
    """
    n: número de municipios
    conexiones: lista de tuplas (costo, municipio1, municipio2)
    """
    from collections import defaultdict

    # Grafo representado como lista de adyacencia
    grafo = defaultdict(list)
    for costo, u, v in conexiones:
        grafo[u].append((costo, v))
        grafo[v].append((costo, u))  # Es no dirigido

    visitado = [False] * n
    min_heap = []
    resultado = []
    costo_total = 0

    # Comenzar desde el nodo 0 (arbitrario)
    visitado[0] = True
    for costo, v in grafo[0]:
        heapq.heappush(min_heap, (costo, 0, v))

    while min_heap and len(resultado) < n - 1:
        costo, u, v = heapq.heappop(min_heap)
        if not visitado[v]:
            visitado[v] = True
            resultado.append((u, v, costo))
            costo_total += costo
            for siguiente_costo, siguiente_vecino in grafo[v]:
                if not visitado[siguiente_vecino]:
                    heapq.heappush(min_heap, (siguiente_costo, v, siguiente_vecino))

    if len(resultado) != n - 1:
        return "No es posible conectar todos los municipios"
    return resultado, costo_total


# Ejemplo de uso
municipios = 4
conexiones = [
    (4, 0, 1),
    (3, 0, 2),
    (2, 1, 2),
    (6, 1, 3),
    (5, 2, 3)
]

resultado = prim(municipios, conexiones)

if isinstance(resultado, str):
    print(resultado)
else:
    conexiones_usadas, costo_total = resultado
    print("Conexiones seleccionadas para minimizar costo:")
    for u, v, costo in conexiones_usadas:
        print(f"Municipio {u} <->  Municipio {v}, Costo: {costo}")
    print(f"Costo total minimo: {costo_total} pesos")
