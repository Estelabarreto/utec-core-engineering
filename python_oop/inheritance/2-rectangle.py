#!/usr/bin/env python3
"""Módulo que define la clase Rectangle heredando de BaseGeometry,
con implementación de área y representación en cadena.
"""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo que hereda de BaseGeometry."""

    def __init__(self, width, height):
        """Inicializa un rectángulo con ancho y altura validados."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Retorna la representación formal en cadena del rectángulo."""
        return f"[Rectangle] {self.__width}/{self.__height}"
