#!/usr/bin/env python3
"""Módulo que contiene una función para calcular potencias."""


def pow(a, b):
    """Calcula y devuelve 'a' elevado a la potencia 'b' de forma manual."""
    if b == 0:
        return 1

    result = 1
    exp = abs(b)
    for _ in range(exp):
        result *= a

    if b < 0:
        return 1 / result
    return result
