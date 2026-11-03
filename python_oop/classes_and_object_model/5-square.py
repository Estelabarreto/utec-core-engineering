#!/usr/bin/env python3
"""Definición de la clase Square con método my_print para imprimir el cuadrado."""


class Square:
    """Representa un cuadrado con validación de tamaño, área y método de impresión."""

    def __init__(self, size=0):
        """Inicializa un cuadrado con un tamaño validado.

        Args:
            size (int): El tamaño del cuadrado (por defecto 0).
        """
        self.size = size

    @property
    def size(self):
        """Recupera el valor del tamaño del cuadrado.

        Returns:
            int: El tamaño actual.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Establece y valida el tamaño del cuadrado.

        Args:
            value (int): El nuevo tamaño.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcula y devuelve el área del cuadrado.

        Returns:
            int: El área del cuadrado (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """Imprime en stdout el cuadrado usando el carácter #.

        Si el tamaño es 0, imprime una línea vacía.
        """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
