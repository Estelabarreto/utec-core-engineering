#!/usr/bin/env python3
"""Definición de la clase Square con un atributo privado size."""


class Square:
    """Representa un cuadrado con un tamaño privado."""

    def __init__(self, size):
        """Inicializa un cuadrado con un tamaño dado.

        Args:
            size (int): El tamaño del cuadrado.
        """
        self.__size = size
