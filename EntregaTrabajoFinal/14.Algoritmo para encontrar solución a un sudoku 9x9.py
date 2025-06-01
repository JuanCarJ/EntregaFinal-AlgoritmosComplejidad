from typing import List

# Matriz de 9x9 con números del 1 al 9 o ceros (vacío)
Tablero = List[List[int]]

def resolver_sudoku(tablero: Tablero) -> bool:
    """
    Resuelve un Sudoku 9x9 utilizando el algoritmo de backtracking.
    Modifica el tablero original en el lugar.

    Retorna:
    - True si se encontró una solución válida.
    - False si no hay solución.
    """
    fila, col = encontrar_casilla_vacia(tablero)
    if fila is None:
        return True  # No hay más espacios vacíos significa que el tablero fue resuelto

    for num in range(1, 10):
        if es_valido(tablero, num, fila, col):
            tablero[fila][col] = num  # Intentamos colocar el número

            if resolver_sudoku(tablero):  # Continuamos con la siguiente casilla
                return True

            tablero[fila][col] = 0  # Deshacemos el intento

    return False  # Ningún número fue válido en esta casilla

def encontrar_casilla_vacia(tablero: Tablero) -> tuple[int | None, int | None]:

    #Busca una casilla vacía (con valor 0) en el tablero.
    
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return i, j
    return None, None

def es_valido(tablero: Tablero, num: int, fila: int, col: int) -> bool:

    #Verifica si colocar 'num' en la posición (fila, col) es válido.

    # Verificar fila
    if num in tablero[fila]:
        return False

    # Verificar columna
    if num in [tablero[i][col] for i in range(9)]:
        return False

    # Verificar subcuadro 3x3
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_col + j] == num:
                return False

    return True

def imprimir_tablero(tablero: Tablero) -> None:

    #Imprime el tablero de Sudoku.

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(tablero[i][j] if tablero[i][j] != 0 else ".", end=" ")
        print()

# Ejemplo de uso
if __name__ == "__main__":
    tablero_sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku original:")
    imprimir_tablero(tablero_sudoku)

    if resolver_sudoku(tablero_sudoku):
        print("\nSolución encontrada:")
        imprimir_tablero(tablero_sudoku)
    else:
        print("\nNo se encontró solución.")
