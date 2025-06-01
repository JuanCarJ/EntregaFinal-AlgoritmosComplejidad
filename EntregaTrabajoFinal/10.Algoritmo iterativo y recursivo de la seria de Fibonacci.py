
def fibonacci_iterativo(n):
    lista = []
    #Caso base
    #Si k es 0, devuelve 0; si k es 1, devuelve 1.
    a, b = 0, 1
    for _ in range(n):
        lista.append(a)
        a, b = b, a + b
    print("Serie de Fibonacci (Iterativa):", lista)
def fibonacci_recursivo(n):
    def fib(k):
        #Caso base
        #Si k es 0, devuelve 0; si k es 1, devuelve 1.
        if k == 0:
            return 0
        elif k == 1:
            return 1
        else:
            return fib(k-1) + fib(k-2)

    lista = [fib(i) for i in range(n)]
    print("Serie de Fibonacci (Recursiva):", lista)

fibonacci_iterativo(10)
fibonacci_recursivo(10)
