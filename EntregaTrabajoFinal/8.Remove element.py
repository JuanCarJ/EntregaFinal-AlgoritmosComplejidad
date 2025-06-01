def quicksort(unsorted):
    """
    Para resolver estre problema, utilizamos el algoritmo Quicksort para ordenar la lista de números que nos den
    """
    if len(unsorted) <= 1:
        return unsorted
    else:
        puntoMedio = unsorted[len(unsorted) // 2]
        menores = [num for num in unsorted if num < puntoMedio]
        iguales = [num for num in unsorted if num == puntoMedio]
        mayores = [num for num in unsorted if num > puntoMedio]
        return quicksort(menores) + iguales + quicksort(mayores)


def removeElement(nums, val):
    """
    El enunciado del ejercicio nos pide que, dado un arreglo nums y un valor val,
    eliminemos todas las apariciones de val en el mismo arreglo y devolvamos la nueva longitud (k),
    donde los primeros k elementos no deben contener val. No importa qué quede después de k.

    Para mayor eficiencia ordenamos la lista y luego recorremos la lista para eliminar los elementos iguales a val.

    Retorna:
    - Un entero k, que representa la cantidad de elementos distintos a val.
    - Los primeros k elementos de nums modificados.
    """
    nums[:] = quicksort(nums) 

    k = 0  # Contador de elementos distintos a val
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


# Ejemplo de uso
nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print(k)          
print(nums[:k])   
