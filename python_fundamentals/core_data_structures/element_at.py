#!/usr/bin/env python3
"""Módulo para recuperar un elemento de una lista de forma segura."""


def element_at(my_list, idx):
    """Devuelve el elemento en la posición idx, o None si es inválido o negativo."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
