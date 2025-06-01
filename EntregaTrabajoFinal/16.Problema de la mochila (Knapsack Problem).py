from typing import List

# Esta clase representa la solución del problema de la mochila
# Incluye el valor máximo total que se puede obtener y la lista de ítems seleccionados
class KnapsackSolution:
    def __init__(self, valorMax: int, itemsSeleccionados: List[int]):
        self.valorMax = valorMax              # Valor total que se logra al llenar la mochila de la mejor manera
        self.itemsSeleccionados = itemsSeleccionados    # Índices de los ítems seleccionados

# Esta clase contiene el algoritmo para resolver el problema de la Mochila
# Dado un conjunto de ítems con valores y pesos, se busca seleccionar los ítems que maximicen el valor total
# sin superar la capacidad máxima de la mochila
class Knapsack:
    @staticmethod
    def solve(valores: List[int], pesos: List[int], capacidad: int) -> KnapsackSolution:
        n = len(valores)  # Cantidad de ítems disponibles

        # dp[i][w] almacenará el valor máximo que se puede obtener usando los primeros i ítems con capacidad w
        dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):         # Recorremos cada ítem
            for w in range(1, capacidad + 1):  # Recorremos cada posible capacidad desde 1 hasta la total
                if pesos[i - 1] > w:
                    # Si el peso del ítem actual excede la capacidad actual, no podemos incluirlo
                    dp[i][w] = dp[i - 1][w]
                else:
                    # Decidimos si incluir o no el ítem actual, comparando el valor de ambas opciones
                    dp[i][w] = max(
                        dp[i - 1][w],  # No incluir el ítem
                        valores[i - 1] + dp[i - 1][w - pesos[i - 1]]  # Incluir ítem
                    )

        # Recuperamos los ítems que fueron seleccionados en la solución óptima
        itemsSeleccionados = []
        current_weight = capacidad

        # Empezamos desde el final de la tabla para reconstruir la decisión
        for i in range(n, 0, -1):
            # Si el valor actual difiere del valor anterior, significa que este ítem fue incluido
            if dp[i][current_weight] != dp[i - 1][current_weight]:
                itemsSeleccionados.append(i - 1)  # Guardamos el índice original del ítem
                current_weight -= pesos[i - 1]  # Reducimos el peso disponible en la mochila

        # Retornamos una instancia con el resultado final
        return KnapsackSolution(dp[n][capacidad], itemsSeleccionados)

# Ejemplo de uso del algoritmo
if __name__ == "__main__":
    # Lista de valores de los ítems (ganancia que obtenemos por llevar ese ítem)
    valores = [3, 4, 5]

    # Lista de pesos correspondientes a cada ítem (cuánto espacio ocupan en la mochila)
    pesos = [2, 3, 4]

    # Capacidad total de la mochila
    capacidad = 5

    # Ejecutamos el algoritmo
    solution = Knapsack.solve(valores, pesos, capacidad)

    # Mostramos el resultado de manera clara
    print(f"Valor máximo que se puede obtener: {solution.valorMax}")
    print("Índices de ítems seleccionados:", ", ".join(map(str, solution.itemsSeleccionados)))
