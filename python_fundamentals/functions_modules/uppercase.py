#!/usr/bin/env python3
"""Módulo que contiene una función para convertir cadenas a mayúsculas."""


def uppercase(str):
    """Imprime la cadena en mayúsculas usando lógica ASCII."""
    for c in str:
        code = ord(c)
        if 97 <= code <= 122:
            c = chr(code - 32)
        print("{}".format(c), end="")
    print("")
