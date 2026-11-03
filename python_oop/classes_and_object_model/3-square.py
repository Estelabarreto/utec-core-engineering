#!/usr/bin/env python3
"""Definición de la clase Square con validación de tamaño y cálculo de área."""


class Square:
    """Representa un cuadrado con tamaño privado validado y cálculo de área."""

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

    def area(self):
        """Calcula y devuelve el área del cuadrado.

        Returns:
            int: El área del cuadrado (size * size).
        """
        return self.__size * self.__size
