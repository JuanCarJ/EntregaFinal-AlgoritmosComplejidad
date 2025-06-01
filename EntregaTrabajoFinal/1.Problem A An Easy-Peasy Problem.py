
def EasyProblem(entrada):
    partes = entrada.split()
    s1 = int(partes[0])
    s2 = int(partes[1])
    
    if s1 * 2 >= s2:
        return "E"
    else:
        return "H"
entrada = "6 13"
resultado = EasyProblem(entrada)
print(resultado)