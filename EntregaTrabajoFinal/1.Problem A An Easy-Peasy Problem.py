
def EasyProblem(entrada):
    partes = entrada.split()
    s1 = int(partes[0])
    s2 = int(partes[1])
    # Verifica si el doble de s1 es mayor o igual a s2
    if s1 * 2 >= s2:
        #Si es mayor o igual, devuelve "E"
        return "E"
    else:
        #Sino H
        return "H"
entrada = "6 13"
resultado = EasyProblem(entrada)
print(resultado)