def busqueda_binaria(lista, objetivo):
    """
    Busca un elemento en una lista ordenada usando el algoritmo de búsqueda binaria. que consiste en
    dividir la lista en dos mitades y descartar una de ellas en cada iteración. 

    Condicion: la lista debe estar ordenada en orden ascendente.

    Parámetros:
    - lista: Lista de elementos en orden ascendente.
    - objetivo: Valor que se quiere encontrar.

    Retorna:
    - El índice donde se encuentra el objetivo si está en la lista.
    - -1 si el objetivo no está presente.
    """

    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        # Se calcula la posición central del rango actual
        medio = (izquierda + derecha) // 2

        # Si encontramos el objetivo, lo devolvemos
        if lista[medio] == objetivo:
            return medio
        # Si el objetivo está a la derecha
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        # Si el objetivo está a la izquierda
        else:
            derecha = medio - 1

    # Si no se encuentra el objetivo
    return -1

# Ejemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
objetivo = 5

resultado = busqueda_binaria(lista, objetivo)
print("Índice del objetivo:", resultado)  
