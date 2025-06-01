def quicksort(unsorted):
    """
    Ordena una lista usando el algoritmo Quicksort, que consiste en:
    - Elegir un elemento llamado pivote.
    - Dividir la lista en tres partes: menores, iguales y mayores al pivote.
    - Aplicar recursivamente el mismo proceso a las sublistas menores y mayores.

    Este algoritmo no requiere que la lista esté ordenada previamente.

    Parámetros:
    - unsorted: Lista desordenada de números (enteros o flotantes).

    Retorna:
    - Una nueva lista con los elementos ordenados de menor a mayor.
    """

    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(unsorted) <= 1:
        return unsorted
    else:
        # Elegimos el elemento del medio como pivote
        puntoMedio = unsorted[len(unsorted) // 2]

        # Sublista con los elementos menores al pivote
        menores = [num for num in unsorted if num < puntoMedio]

        # Sublista con los elementos iguales al pivote
        iguales = [num for num in unsorted if num == puntoMedio]

        # Sublista con los elementos mayores al pivote
        mayores = [num for num in unsorted if num > puntoMedio]

        # Aplicamos quicksort recursivamente a las sublistas y las unimos
        return quicksort(menores) + iguales + quicksort(mayores)


# Ejemplo de uso
unsorted = [3, 6, 8, 10, 1, 2, 1]

result = quicksort(unsorted)

# Mostramos la lista ya ordenada
print("Lista ordenada:", result)  # Debería imprimir: [1, 1, 2, 3, 6, 8, 10]
