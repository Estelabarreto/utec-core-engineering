#!/usr/bin/env python3
"""Definición de la clase Square con
size, position, area, my_print y __str__.
"""


class Square:
    """Representa un cuadrado con tamaño,
    posición, área y representación en cadena.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un cuadrado con
        tamaño y posición validados.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Recupera el tamaño."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece y valida el tamaño."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Recupera la posición."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece y valida la posición."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                isinstance(value[0], bool) or
                not isinstance(value[1], int) or
                isinstance(value[1], bool) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Calcula y devuelve el área."""
        return self.__size * self.__size

    def __str__(self):
        """Retorna la representación en cadena del cuadrado."""
        if self.__size == 0:
            return ""
        s = []
        for _ in range(self.__position[1]):
            s.append("")
        for _ in range(self.__size):
            s.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(s)

    def my_print(self):
        """Imprime en stdout el cuadrado."""
        print(self)
