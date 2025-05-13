def entregaDinero(monto_solicitado):
    # Paso 0: Validación inicial
    # Si el monto no es múltiplo de 10000, mostramos un mensaje de error.
    if monto_solicitado % 10000 != 0:
        return "Error: El monto debe ser divisible por 10000"

    # Paso 1: Definimos las denominaciones de billetes disponibles (de mayor a menor)
    denominaciones = [100000, 50000, 20000, 10000]

    # Definimos cuántos billetes hay disponibles de cada denominación
    disponibilidad = {
        100000: 50,   
        50000: 100,   
        20000: 200,   
        10000: 300    
    }

    # Creamos un diccionario vacío donde guardaremos los billetes entregados
    billetes_entregados = {}

    # Paso 2: Algoritmo voraz 
    # Intentamos usar primero los billetes de mayor valor para completar el monto
    for billete in denominaciones:
        # Si ya entregamos el monto completo, salimos del ciclo
        if monto_solicitado <= 0:
            break

        # Calculamos cuántos billetes de este tipo se necesitarían
        max_billetes_necesarios = monto_solicitado // billete

        # Elegimos la menor cantidad entre lo que necesitamos y lo que hay disponible
        billetes_a_entregar = min(max_billetes_necesarios, disponibilidad[billete])

        # Guardamos cuántos billetes de este tipo vamos a entregar
        billetes_entregados[billete] = billetes_a_entregar

        # Restamos al monto lo que ya se entregó
        monto_solicitado -= billetes_a_entregar * billete

    # Paso 3: Verificamos si se pudo entregar todo el monto
    if monto_solicitado > 0:
        # Si aún queda algo por entregar, no fue posible dar el dinero completo
        return "No hay suficiente cantidad de billetes para entregar el dinero solicitado"

    # Si todo se entregó correctamente, devolvemos el detalle de billetes entregados
    return billetes_entregados

# PRUEBA DEL PROGRAMA
monto = 20000000 
resultado = entregaDinero(monto)

# Si el resultado es un diccionario
if isinstance(resultado, dict):
    # Mostramos el monto solicitado
    print(f"Monto solicitado: {monto}")
    # Mostramos cuántos billetes de cada denominación fueron entregados
    for denominacion in sorted(resultado.keys(), reverse=True):
        print(f"Billetes de {denominacion}: {resultado[denominacion]}")
else:
    # Si no fue posible entregar el dinero, se muestra el mensaje de error
    print(resultado)
