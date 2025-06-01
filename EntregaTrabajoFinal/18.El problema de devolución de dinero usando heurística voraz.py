from typing import List, Tuple

def cambio_voraz(monedas, monto: int):
    """
    Algoritmo voraz para devuelta con la menor cantidad de monedas posible,
    usando siempre la moneda de mayor valor que no exceda el monto restante.

    Parámetros:
    - monedas: Lista de valores de monedas disponibles
    - monto: Valor total del cambio que se desea entregar

    Retorna:
    - Una tupla con:
        - cantidad total de monedas utilizadas
        - lista de monedas utilizadas
    """
    # Ordenamos las monedas de mayor a menor para aplicar la heurística voraz
    monedas.sort(reverse=True)
    
    usadas = []  # Lista de monedas que vamos seleccionando
    restante = monto

    # Mientras quede devuelta por cubrir
    for moneda in monedas:
        # Mientras podamos usar esta moneda
        while moneda <= restante:
            usadas.append(moneda)
            restante -= moneda

    return len(usadas), usadas

# Ejemplo de uso
if __name__ == "__main__":
    monedas_disponibles = [1, 5, 10, 25]
    monto_a_devolver = 63

    cantidad, usadas = cambio_voraz(monedas_disponibles, monto_a_devolver)

    print(f"Monedas utilizadas: {cantidad}")
    print("Detalle:", usadas)
