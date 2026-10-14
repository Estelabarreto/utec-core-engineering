#!/usr/bin/env python3
"""Módulo para agregar o actualizar una clave/valor en un diccionario."""


def update_dictionary(a_dictionary, key, value):
    """Reemplaza o agrega un par clave/valor en el diccionario y lo devuelve."""
    a_dictionary[key] = value
    return a_dictionary
