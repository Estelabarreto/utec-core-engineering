#!/usr/bin/env python3
"""Módulo para imprimir y devolver último dígito."""


def print_last_digit(number):
    """Imprime y devuelve el último dígito."""
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
