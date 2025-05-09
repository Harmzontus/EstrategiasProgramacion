def countSmallerElements(numeros):
    # Paso 1: Asociar cada número con su índice original
    indexed_nums = list(enumerate(numeros))  # [(0, 5), (1, 2), (2, 6), (3, 1), (4, 3)]
    n = len(numeros)
    result = [0] * n  # Lista para guardar el resultado final

    def merge_sort(enum):
        mid = len(enum) // 2
        if mid:
            left = merge_sort(enum[:mid])     # Divide izquierda
            right = merge_sort(enum[mid:])    # Divide derecha
            merged = []
            i = j = 0
            right_count = 0  # Número de elementos menores en right

            # Merge personalizado con conteo
            while i < len(left) and j < len(right):
                if left[i][1] > right[j][1]:
                    # Como right[j][1] < left[i][1], suma al contador
                    result[left[i][0]] += len(right) - j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            # Añadir lo que queda
            merged += left[i:]
            merged += right[j:]
            return merged
        return enum

    merge_sort(indexed_nums)
    return result

# Ejemplo de prueba
numeros = [5, 2, 6, 1, 3]
output = countSmallerElements(numeros)

print("Entrada:", numeros)
print("Salida:", output)
