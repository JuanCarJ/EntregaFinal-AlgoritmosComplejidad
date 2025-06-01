def isPalindrome(x):
    """
    El enunciado nos pide verificar si un número entero es un palíndromo.

    Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda.
    Para ello, se convierte el número a cadena y se compara con su versión invertida.

    Parámetros:
    - x: Número entero a evaluar.

    Retorna:
    - True si el número es palíndromo.
    - False en caso contrario.
    """

    S = str(x) 

    if S == S[::-1]:
        return True
    else:
        return False


# Ejemplo de uso
x = 121
result = isPalindrome(x)
print("El número", x, "es palíndromo:", result)  # Debería imprimir: True
