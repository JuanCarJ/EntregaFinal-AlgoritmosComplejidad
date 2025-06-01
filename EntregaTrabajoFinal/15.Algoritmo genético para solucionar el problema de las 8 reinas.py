import random
import tkinter as tk

TAMANO_POBLACION = 100
MAX_GENERACIONES = 500
PROB_MUTACION = 0.00000001


def generar_cromosoma():
    cromosoma = list(range(8))
    random.shuffle(cromosoma)
    return cromosoma

def calcular_fitness(cromosoma):
    conflictos = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(i - j) == abs(cromosoma[i] - cromosoma[j]):
                conflictos += 1
    return conflictos

def cruzar(padre, madre):
    punto_corte = random.randint(1, 6)
    hijo = padre[:punto_corte]
    for gen in madre:
        if gen not in hijo:
            hijo.append(gen)
    return hijo

def mutar(cromosoma):
    if random.random() < PROB_MUTACION:
        i, j = random.sample(range(8), 2)
        cromosoma[i], cromosoma[j] = cromosoma[j], cromosoma[i]
    return cromosoma

def seleccionar_padres(poblacion, fitnesses):
    torneo = random.sample(list(zip(poblacion, fitnesses)), 5)
    torneo.sort(key=lambda x: x[1])
    return torneo[0][0], torneo[1][0]

def imprimir_matriz(cromosoma):
    matriz = [['O' for _ in range(8)] for _ in range(8)]
    for fila in range(8):
        columna = cromosoma[fila]
        matriz[fila][columna] = 'R'
    for fila in matriz:
        print(' '.join(fila))

def mostrar_tablero_tk(cromosoma, generacion):
    def recargar():
        root.destroy()
        algoritmo_genetico()

    root = tk.Tk()
    root.title("Solucion Juan")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    size = 50
    for i in range(8):
        for j in range(8):
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(j*size, i*size, (j+1)*size, (i+1)*size, fill=color)

    for fila in range(8):
        col = cromosoma[fila]
        x = col * size + size // 2
        y = fila * size + size // 2
        canvas.create_text(x, y, text="♛", font=("Arial", 28), fill="red")

    etiqueta = tk.Label(root, text=f"Generacion: {generacion}", font=("Arial", 14))
    etiqueta.pack(pady=10)

    boton = tk.Button(root, text="Recargar solucion", command=recargar, font=("Arial", 12))
    boton.pack(pady=5)

    root.mainloop()

def algoritmo_genetico():
    poblacion = [generar_cromosoma() for _ in range(TAMANO_POBLACION)]
    for generacion in range(1, MAX_GENERACIONES + 1):
        fitnesses = [calcular_fitness(ind) for ind in poblacion]

        if 0 in fitnesses:
            index = fitnesses.index(0)
            solucion = poblacion[index]
            print(f"\nSolucion encontrada en la generacion {generacion}:")
            imprimir_matriz(solucion)
            print("\nCromosoma solucion:", solucion)
            mostrar_tablero_tk(solucion, generacion)
            return solucion

        nueva_poblacion = []
        while len(nueva_poblacion) < TAMANO_POBLACION:
            padre, madre = seleccionar_padres(poblacion, fitnesses)
            hijo = cruzar(padre, madre)
            hijo = mutar(hijo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    print("\nNo se encontro solucion en el limite de generaciones.")
    return None

# Ejecutar el algoritmo genetico
algoritmo_genetico()
