#!/usr/bin/env python3
"""Módulo que contiene una función para convertir cadenas a mayúsculas."""


def uppercase(str):
    """Imprime la cadena en mayúsculas usando lógica ASCII."""
    result = ""
    for c in str:
        code = ord(c)
        if 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += c
    print(result)
