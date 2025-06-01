def factorial_iterativo(n):
    """
    Calcula el factorial de un número entero no negativo de forma iterativa.

    El factorial de un número n (n!) es el producto de todos los enteros positivos desde 1 hasta n.
    Por definición, 0! = 1.

    Parámetros:
    - n (int): número entero >= 0

    Retorna:
    - int: el valor de n!

    Lanza:
    - ValueError: si n es menor que 0.
    """
    if n < 0:
        raise ValueError("n debe ser >= 0")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def factorial_recursivo(n):
    """
    Calcula el factorial de un número entero no negativo usando recursión.

    La función se llama a sí misma para calcular el valor de n!, cumpliendo:
    - Caso base: 0! y 1! son 1
    - Caso recursivo: n! = n * (n-1)!

    Parámetros:
    - n (int): número entero >= 0

    Retorna:
    - int: el valor de n!

    Lanza:
    - ValueError: si n es menor que 0.
    """
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n <= 1:
        return 1
    return n * factorial_recursivo(n - 1)


if __name__ == "__main__":
    # Ejemplo: cálculo de factoriales del 0 al 5 con ambos métodos
    for i in range(6):
        print(f"Iterativo {i}! = {factorial_iterativo(i)}")


    for i in range(6):
        print(f"Recursivo {i}! = {factorial_recursivo(i)}")
