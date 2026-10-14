#!/usr/bin/env python3
"""Módulo que contiene una función para imprimir enteros de una lista."""


def print_list_integer(my_list=[]):
    """Imprime todos los enteros de una lista usando formato :d."""
    for i in my_list:
        print("{:d}".format(i))
