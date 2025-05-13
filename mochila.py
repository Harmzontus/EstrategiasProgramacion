# Definimos una clase llamada Objeto
# Esta clase representa un objeto con nombre, peso y valor
class Objeto:
    # Método constructor: se llama automáticamente cuando se crea un objeto de esta clase
    def __init__(self, nombre, peso, valor):
        self.nombre = nombre  # Guardamos el nombre del objeto
        self.peso = peso      # Guardamos el peso del objeto
        self.valor = valor    # Guardamos el valor del objeto

    # Método para calcular el valor por unidad de peso del objeto
    def valor_unitario(self):
        # Si el peso es distinto de cero, se calcula normalmente
        # Si el peso es cero, se devuelve 0 para evitar división por cero
        return self.valor / self.peso if self.peso != 0 else 0


# Función principal que implementa el algoritmo de la mochila fraccionaria
def mochila_fraccionaria(objetos, capacidad_maxima, heuristica):
    # Paso 1: Ordenamos los objetos según la heurística elegida

    if heuristica == 'valor_unitario':
        # Ordenamos por valor por peso (más eficiente primero)
        objetos.sort(key=lambda x: x.valor_unitario(), reverse=True)
    elif heuristica == 'valor':
        # Ordenamos por valor total (sin importar el peso)
        objetos.sort(key=lambda x: x.valor, reverse=True)
    elif heuristica == 'peso':
        # Ordenamos por peso (los más livianos primero)
        objetos.sort(key=lambda x: x.peso)
    else:
        # Si se pasa una heurística no válida, lanzamos un error
        raise ValueError("Heurística no válida")

    # Paso 2: Inicializamos variables para controlar el estado del proceso
    peso_actual = 0          # Cuánto peso llevamos en la mochila
    valor_total = 0          # Cuánto valor hemos acumulado
    seleccionados = []       # Lista para guardar los objetos seleccionados

    # Paso 3: Recorremos los objetos ordenados
    for obj in objetos:
        # Si aún cabe todo el objeto completo
        if peso_actual + obj.peso <= capacidad_maxima:
            peso_actual += obj.peso              # Agregamos el peso del objeto
            valor_total += obj.valor             # Sumamos su valor al total
            seleccionados.append((obj.nombre, obj.peso, obj.valor))  # Lo registramos
        else:
            # Si no cabe completo, intentamos agregar una fracción del objeto
            peso_restante = capacidad_maxima - peso_actual
            if peso_restante > 0:
                fraccion = peso_restante / obj.peso
                valor_fraccionado = obj.valor * fraccion
                peso_actual += peso_restante
                valor_total += valor_fraccionado
                seleccionados.append((obj.nombre, peso_restante, valor_fraccionado))
            break  # Una vez llena la mochila, salimos del ciclo

    # Devolvemos la lista de objetos seleccionados y el valor total acumulado
    return seleccionados, valor_total


# -----------------------------
# PRUEBA DEL ALGORITMO
# -----------------------------

# Creamos una lista de objetos con diferentes pesos y valores
objetos = [
    Objeto("Objeto1", 10, 60),
    Objeto("Objeto2", 20, 100),
    Objeto("Objeto3", 30, 120)
]

# Definimos la capacidad máxima de la mochila (por ejemplo, 50 kg)
capacidad = 50

# Probamos el algoritmo usando tres heurísticas diferentes
for heur in ['valor_unitario', 'valor', 'peso']:
    print(f"\n--- Heurística: {heur} ---")

    # Llamamos a la función y guardamos el resultado
    seleccionados, valor_total = mochila_fraccionaria(objetos.copy(), capacidad, heur)

    # Mostramos los objetos que fueron seleccionados
    for nombre, peso, valor in seleccionados:
        print(f"{nombre}: {peso:.1f} kg, Valor: {valor:.1f}")

    # Mostramos el valor total que se logró obtener
    print(f"Valor total de la carga: {valor_total:.1f}")
