#!/usr/bin/env python3
"""Definición de la clase Rectangle con
anchura, altura, validaciones, área y perímetro.
"""


class Rectangle:
    """Representa un rectángulo con anchura, altura,
    métodos para calcular área y perímetro.
    """

    def __init__(self, width=0, height=0):
        """Inicializa un rectángulo con anchura y altura opcionales."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Recupera la anchura del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece y valida la anchura del rectángulo."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Recupera la altura del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece y valida la altura del rectángulo."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcula y devuelve el perímetro del rectángulo.

        Si width o height es 0, el perímetro es 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
