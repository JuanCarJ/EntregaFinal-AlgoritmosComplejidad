
B = input()
B = B.split()

# Convertimos los valores a enteros y verificamos si el número de soluciones
# en la primera mitad del concurso es al menos la mitad del total de soluciones
if int(B[0]) >= int(B[1]) / 2:
    print("E")  # Problema considerado fácil acorde al enunciado
else:
    print("H")  # Problema considerado difícil acorde al enunciado

C = input()
C = C.split()

# Asignamos las edades de Dr. O, Alyssa y Konari a variables.
AgeDr = int(C[0])  # Edad del Dr. O
AgeA = int(C[1])   # Edad de Alyssa
AgeK = int(C[2])   # Edad de Konari

# Inicializamos una bandera para indicar si se encontró una combinación válida
flag = False

# Probar todas las combinaciones posibles de a y k mayores que cero. Comenzamos desde 1 ya que a y k deben ser estrictamente mayores que 0
for i in range(1, AgeDr + 1):
    for j in range(1, AgeDr + 1):
        if AgeA * i + AgeK * j == AgeDr:
            flag = True
            break  # Sale del bucle interno si se encuentra una solución
    if flag:
        break  # Salir del bucle externo si ya se encontró una solución para ahorrar tiempo computacional

# Imprimir 1 si existe una combinación válida, de lo contrario imprimir 0
if flag:
    print("1")
else:
    print("0")
