#!/usr/bin/env python3
"""Módulo para reemplazar un elemento en una lista de forma segura."""


def replace_in_list(my_list, idx, element):
    """Reemplaza el elemento en idx si es válido, si no, devuelve la lista."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
