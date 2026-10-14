#!/usr/bin/env python3
"""Módulo para imprimir una matriz de enteros."""


def print_matrix_integer(matrix=[[]]):
    """Imprime una matriz de enteros formateada con espacios."""
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
