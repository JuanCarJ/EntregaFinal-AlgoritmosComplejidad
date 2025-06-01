def superDigit(n, k=1):
    # Caso inicial donde se debe operar n * k para obtener el numero a operar.
    if k != 1:
        suma_inicial = sum(int(d) for d in n) * k
        return superDigit(str(suma_inicial))  # Continúa con k=1
    
    # Paso 2: Caso base si n es un solo dígito
    if len(n) == 1:
        return int(n)
    #Suma de los numeros
    suma = sum(int(d) for d in n)
    return superDigit(str(suma))
