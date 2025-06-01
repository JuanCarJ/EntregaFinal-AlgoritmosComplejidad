def busqueda_lineal(lista, elementoABuscar):
    #Se recorre la lista y se compara cada elemento con el elementoABuscar a encontrar
    for i in range(len(lista)):
        if lista[i] == elementoABuscar:
            #Si se encuentra el elemento, se devuelve su indice
            return i
    return -1
# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
elementoABuscar = 3
#Devuelve el indice del elemento buscado
resultado = busqueda_lineal(lista, elementoABuscar)