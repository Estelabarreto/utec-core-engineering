#!/usr/bin/env python3
"""Módulo para sumar dos tuplas considerando hasta sus dos primeros elementos."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Suma dos tuplas tomando como máximo sus primeros 2 elementos (0 si faltan)."""
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a1 + b1, a2 + b2)
