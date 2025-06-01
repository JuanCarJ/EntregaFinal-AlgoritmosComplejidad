def quicksort(unsorted):
        if len(unsorted) <= 1:
            return unsorted
        else:
            puntoMedio = unsorted[len(unsorted) // 2]
            menores = [num for num in unsorted if num < puntoMedio]
            iguales = [num for num in unsorted if num == puntoMedio]
            mayores = [num for num in unsorted if num > puntoMedio]
            return quicksort(menores) + iguales + quicksort(mayores)
unsorted = [3, 6, 8, 10, 1, 2, 1]
result = quicksort(unsorted)
print("Lista ordenada:", result)