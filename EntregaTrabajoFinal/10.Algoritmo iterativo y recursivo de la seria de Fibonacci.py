#!/usr/bin/env python3
# -- coding: utf-8 --

"""
Contiene dos funciones para calcular F(n) de la serie de Fibonacci:
1. fibonacci_iterativo(n): versión iterativa (O(n)).
2. fibonacci_recursivo(n): versión recursiva directa (O(2^n)).
"""

def fibonacci_iterativo(n):
    """Retorna F(n) usando un bucle iterativo. F(0)=0, F(1)=1."""
    if n < 0:
        raise ValueError("n debe ser >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_recursivo(n):
    """Retorna F(n) usando la definición recursiva. No optimizada."""
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n < 2:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

if _name_ == "_main_":
    # Ejemplos breves
    for i in range(6):
        print(f"Iterativo F({i}) = {fibonacci_iterativo(i)}")
    print()
    for i in range(6):
        print(f"Recursivo F({i}) = {fibonacci_recursivo(i)}")