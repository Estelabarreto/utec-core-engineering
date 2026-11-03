#!/usr/bin/env python3
"""Módulo que define la clase base BaseGeometry para figuras geométricas."""


class BaseGeometry:
    """Clase base que proporciona funcionalidad compartida
    para figuras geométricas.
    """

    def area(self):
        """Método que calcula el área de la figura geométrica.

        Raises:
            Exception: Indica que el método no está implementado.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea un entero mayor que 0.

        Args:
            name (str): Nombre del parámetro a validar.
            value: Valor a comprobar.

        Raises:
            TypeError: Si value no es un entero (o es booleano).
            ValueError: Si value es menor o igual a 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
