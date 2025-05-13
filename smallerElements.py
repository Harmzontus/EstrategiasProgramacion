def countSmallerElements(numeros):
    # Asociamos cada número con su posición original usando enumerate.
    # Esto crea una lista de tuplas
    indexed_nums = list(enumerate(numeros))  

    # Guardamos la cantidad de elementos en la lista
    n = len(numeros)

    # Creamos una lista de ceros que usaremos para guardar la respuesta final.
    result = [0] * n  

    # Definimos una función interna llamada merge_sort para ordenar y contar
    def merge_sort(enum):
        # Calculamos el punto medio de la lista actual
        mid = len(enum) // 2

        # Si la lista tiene más de un elemento, la seguimos dividiendo
        if mid:
            # Dividimos la lista en dos partes
            left = merge_sort(enum[:mid])     # Parte izquierda 
            right = merge_sort(enum[mid:])    # Parte derecha 

            # Lista para almacenar la mezcla ordenada
            merged = []
            # i y j son índices para recorrer las listas left y right
            i = j = 0
            # Esta variable cuenta cuántos elementos menores hemos visto en la derecha
            right_count = 0  

            # Mezclamos las dos partes ordenadas comparando elementos
            while i < len(left) and j < len(right):
                # Si el valor en left es mayor al de right,
                # entonces los elementos restantes en right son menores
                if left[i][1] > right[j][1]:
                    # Sumamos al resultado en la posición original del número de la izquierda
                    result[left[i][0]] += len(right) - j
                    # Agregamos el elemento de left a la lista combinada
                    merged.append(left[i])
                    # Avanzamos en la lista left
                    i += 1
                else:
                    # Si no, simplemente agregamos el elemento de right
                    merged.append(right[j])
                    # Avanzamos en la lista right
                    j += 1

            # Cuando terminan las comparaciones, agregamos lo que quedó en left y right
            merged += left[i:]   # Agregamos los elementos restantes de left
            merged += right[j:]  # Agregamos los elementos restantes de right

            # Devolvemos la lista combinada y ordenada
            return merged

        # Si la lista tiene solo un elemento, se devuelve como está
        return enum

    # Llamamos a merge_sort con la lista de números indexados
    merge_sort(indexed_nums)

    # Devolvemos la lista con los resultados (números menores a la derecha)
    return result

# --- Ejemplo de uso ---

# Lista de entrada
numeros = [5, 2, 6, 1, 3]

# Llamamos a la función y guardamos la salida
output = countSmallerElements(numeros)

# Imprimimos los resultados
print("Entrada:", numeros)  # Lista original
print("Salida:", output)    # Lista con conteos de números menores a la derecha
