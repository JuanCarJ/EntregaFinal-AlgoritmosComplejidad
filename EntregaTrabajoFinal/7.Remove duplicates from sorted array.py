def removeDuplicates(nums):
    """
    El enunciado del ejercicio nos pide que; dado un arreglo de enteros nums ordenado en orden no decreciente, 
    eliminar los elementos duplicados en la mismo lista de forma que cada elemento único aparezca solo una vez y se mantenga el orden relativo.

    El algoritmo debe modificar el arreglo nums tal que los primeros k elementos 
    contengan los elementos únicos, y luego retorna ese valor k.

    No importa qué valores queden después de los primeros k elementos.

    Ejemplo:
    Input:  nums = [1, 1, 2]
    Output: k = 2, nums = [1, 2, _]

    Parámetros:
    - nums: Lista de enteros ordenados en forma no decreciente.

    Retorna:
    - k: Número de elementos únicos (longitud lógica del arreglo tras eliminar duplicados).
    """

    Size = len(nums)  # Tamaño del arreglo original

    # Caso base: arreglo vacío
    if Size == 0:
        return 0

    k = 1  # Posición donde se colocará el siguiente elemento único
    i = 1  # Índice actual para recorrer la lista

    # Recorremos desde el segundo elemento
    while i < Size:
        # Si el actual es diferente al anterior, lo colocamos en la posición k
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
        i += 1

    #  Rellenamos el resto con "_"
    RayitasPendientes = Size - k
    for _ in range(RayitasPendientes):
        nums.append("_")

    return k


# Ejemplo de uso
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(nums)

# Imprimir resultados
print("Número de elementos únicos:", k)           # Debería imprimir: 5
print("Arreglo modificado:", nums[:k])            # Debería imprimir: [0, 1, 2, 3, 4]
