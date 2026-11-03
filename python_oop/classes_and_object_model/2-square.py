#!/usr/bin/env python3
"""Definición de la clase Square con validación de tamaño."""


class Square:
    """Representa un cuadrado con validaciones en su tamaño privado."""

    def __init__(self, size=0):
        """Inicializa un cuadrado con un tamaño validado.

        Args:
            size (int): El tamaño del cuadrado (por defecto 0).

        Raises:
            TypeError: Si size no es un entero.
            ValueError: Si size es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
