class Objeto:
    def __init__(self, nombre, peso, valor):
        self.nombre = nombre
        self.peso = peso
        self.valor = valor

    def valor_unitario(self):
        return self.valor / self.peso if self.peso != 0 else 0

def mochila_fraccionaria(objetos, capacidad_maxima, heuristica):
    if heuristica == 'valor_unitario':
        objetos.sort(key=lambda x: x.valor_unitario(), reverse=True)
    elif heuristica == 'valor':
        objetos.sort(key=lambda x: x.valor, reverse=True)
    elif heuristica == 'peso':
        objetos.sort(key=lambda x: x.peso)
    else:
        raise ValueError("Heurística no válida")

    peso_actual = 0
    valor_total = 0
    seleccionados = []

    for obj in objetos:
        if peso_actual + obj.peso <= capacidad_maxima:
            peso_actual += obj.peso
            valor_total += obj.valor
            seleccionados.append((obj.nombre, obj.peso, obj.valor))
        else:
            peso_restante = capacidad_maxima - peso_actual
            if peso_restante > 0:
                fraccion = peso_restante / obj.peso
                valor_fraccionado = obj.valor * fraccion
                peso_actual += peso_restante
                valor_total += valor_fraccionado
                seleccionados.append((obj.nombre, peso_restante, valor_fraccionado))
            break  # El contenedor está lleno

    return seleccionados, valor_total

# Prueba de la aplicación
objetos = [
    Objeto("Objeto1", 10, 60),
    Objeto("Objeto2", 20, 100),
    Objeto("Objeto3", 30, 120)
]

capacidad = 50

for heur in ['valor_unitario', 'valor', 'peso']:
    print(f"\n--- Heuristica: {heur} ---")
    seleccionados, valor_total = mochila_fraccionaria(objetos.copy(), capacidad, heur)
    for nombre, peso, valor in seleccionados:
        print(f"{nombre}: {peso:.1f} kg, Valor: {valor:.1f}")
    print(f"Valor total de la carga: {valor_total:.1f}")
