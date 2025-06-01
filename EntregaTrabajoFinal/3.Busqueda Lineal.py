def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1
# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
objetivo = 3
#Devuelve el indice del elemento buscado
resultado = busqueda_lineal(lista, objetivo)