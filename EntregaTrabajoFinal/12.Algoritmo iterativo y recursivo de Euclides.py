def mcd_iterativo(a, b):
    """
    Calcula el MCD (Máximo Común Divisor) de dos enteros no negativos usando el
    algoritmo de Euclides de forma iterativa.

    El algoritmo se basa en la idea de que:
    - MCD(a, b) = MCD(b, a % b)
    - Cuando b llega a cero, a contiene el MCD.

    Condiciones:
    - Si a < 0 o b < 0, se lanza un ValueError porque el MCD solo está definido para enteros ≥ 0.

    Parámetros:
    - a (int): Primer número entero no negativo.
    - b (int): Segundo número entero no negativo.

    Retorna:
    - int: El MCD de a y b.
    """
    if a < 0 or b < 0:
        raise ValueError("Los parámetros deben ser >= 0")

    # Iteramos hasta que b sea cero. En cada paso, actualizamos a y b con (b, a % b)
    while b:
        a, b = b, a % b
    return a


def mcd_recursivo(a, b):
    """
    Calcula el MCD de forma recursiva

    - Caso base: si b == 0, se retorna a.
    - Caso recursivo: se llama a la función con (b, a % b).

    Condiciones:
    - Si a < 0 o b < 0, se lanza un ValueError porque el MCD solo está definido para enteros ≥ 0.

    Parámetros:
    - a (int): Primer número entero no negativo.
    - b (int): Segundo número entero no negativo.

    Retorna:
    - int: El MCD de a y b.
    """
    if a < 0 or b < 0:
        raise ValueError("Los parámetros deben ser >= 0")

    # Si b es cero, el resultado es a; si no, se continúa recursivamente
    return a if b == 0 else mcd_recursivo(b, a % b)


if __name__ == "__main__":
    ejemplos = [(48, 18), (54, 24), (0, 5), (7, 0), (270, 192)]

    print("Pruebas mcd_iterativo:")
    for x, y in ejemplos:
        print(f"mcd_iterativo({x}, {y}) = {mcd_iterativo(x, y)}")

    print("\nPruebas mcd_recursivo:")
    for x, y in ejemplos:
        print(f"mcd_recursivo({x}, {y}) = {mcd_recursivo(x, y)}")