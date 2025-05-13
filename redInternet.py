import heapq

def prim(n, conexiones):
    """
    n: número de municipios
    conexiones: lista de tuplas (costo, municipio1, municipio2)
    """
    from collections import defaultdict

    # Representamos el grafo como una lista de adyacencia
    grafo = defaultdict(list)
    for costo, u, v in conexiones:
        grafo[u].append((costo, v))  # Agregamos conexión desde u hacia v
        grafo[v].append((costo, u))  # Agregamos conexión desde v hacia u (grafo no dirigido)

    visitado = [False] * n         # Lista para saber qué municipios ya están conectados
    min_heap = []                  # Cola de prioridad para escoger la conexión más barata
    resultado = []                 # Lista de conexiones seleccionadas
    costo_total = 0                # Acumulador del costo total

    # Comenzamos desde el municipio 0 (puede ser cualquiera)
    visitado[0] = True
    # Añadimos todas las conexiones desde el nodo 0 a la cola
    for costo, v in grafo[0]:
        heapq.heappush(min_heap, (costo, 0, v))  # (costo, desde, hacia)

    # Repetimos hasta que conectemos todos los municipios
    while min_heap and len(resultado) < n - 1:
        costo, u, v = heapq.heappop(min_heap)  # Escogemos la conexión más barata
        if not visitado[v]:
            visitado[v] = True  # Marcamos el municipio como conectado
            resultado.append((u, v, costo))  # Guardamos la conexión
            costo_total += costo  # Sumamos el costo

            # Agregamos las conexiones desde el nuevo municipio
            for siguiente_costo, siguiente_vecino in grafo[v]:
                if not visitado[siguiente_vecino]:
                    heapq.heappush(min_heap, (siguiente_costo, v, siguiente_vecino))

    # Verificamos si fue posible conectar todos los municipios
    if len(resultado) != n - 1:
        return "No es posible conectar todos los municipios"

    # Retornamos las conexiones seleccionadas y el costo total
    return resultado, costo_total


# --------------------------
# EJEMPLO DE USO DEL CÓDIGO
# --------------------------

# Número total de municipios (nodos del grafo)
municipios = 4

# Lista de conexiones posibles: (costo, municipio1, municipio2)
conexiones = [
    (4, 0, 1),
    (3, 0, 2),
    (2, 1, 2),
    (6, 1, 3),
    (5, 2, 3)
]

# Ejecutamos el algoritmo de Prim
resultado = prim(municipios, conexiones)

# Mostramos el resultado
if isinstance(resultado, str):
    # Si la función devolvió un mensaje de error
    print(resultado)
else:
    # Si todo salió bien, mostramos las conexiones usadas y el costo total
    conexiones_usadas, costo_total = resultado
    print("Conexiones seleccionadas para minimizar costo:")
    for u, v, costo in conexiones_usadas:
        print(f"Municipio {u} <->  Municipio {v}, Costo: {costo}")
    print(f"Costo total minimo: {costo_total} pesos")
