#!/usr/bin/env python3
"""Módulo que define la clase Square heredando de Rectangle,
con representación en cadena personalizada.
"""


Rectangle = __import__('1-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado que hereda de Rectangle,
    sobrescribiendo la representación en cadena.
    """

    def __init__(self, size):
        """Inicializa un cuadrado con un tamaño validado."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Retorna la representación formal en cadena del cuadrado."""
        return f"[Square] {self.__size}/{self.__size}"
