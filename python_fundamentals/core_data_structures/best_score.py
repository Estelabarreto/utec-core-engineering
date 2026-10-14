#!/usr/bin/env python3
"""Módulo para encontrar la clave con el valor entero más alto."""


def best_score(a_dictionary):
    """Devuelve la clave con el mayor valor entero en el diccionario."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
