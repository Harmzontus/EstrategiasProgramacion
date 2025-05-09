def entregaDinero(monto_solicitado):
    # Validación inicial
    if monto_solicitado % 10000 != 0:
        return "Error: El monto debe ser divisible por 10000"

    # Paso 1: Definimos las denominaciones y su disponibilidad
    denominaciones = [100000, 50000, 20000, 10000]
    disponibilidad = {
        100000: 50,
        50000: 100,
        20000: 200,
        10000: 300
    }

    billetes_entregados = {}

    # Paso 2: Implementacion de Algoritmo voraz
    for billete in denominaciones:
        if monto_solicitado <= 0:
            break

        max_billetes_necesarios = monto_solicitado // billete
        billetes_a_entregar = min(max_billetes_necesarios, disponibilidad[billete])

        billetes_entregados[billete] = billetes_a_entregar
        monto_solicitado -= billetes_a_entregar * billete

    # Paso 3: Verificamos si el monto se pudo entregar completamente
    if monto_solicitado > 0:
        return "No hay suficiente cantidad de billetes para entregar el dinero solicitado"

    return billetes_entregados

# Ejemplo de uso
monto = 20000000 
resultado = entregaDinero(monto)

# Salida
if isinstance(resultado, dict):
    print(f"Monto solicitado: {monto}")
    for denominacion in sorted(resultado.keys(), reverse=True):
        print(f"Billetes de {denominacion}: {resultado[denominacion]}")
else:
    print(resultado)    


