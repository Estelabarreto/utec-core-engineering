#!/usr/bin/env python3
"""Módulo de demostración para herencia y polimorfismo en Python.

Incluye la clase base Animal y las subclases Dog y Cat que sobrescriben
el método speak() para ilustrar el polimorfismo.
"""


class Animal:
    """Clase base que representa a un animal genérico."""

    def speak(self):
        """Retorna el sonido genérico del animal."""
        return "Some sound"


class Dog(Animal):
    """Representa a un perro, heredando de Animal."""

    def speak(self):
        """Retorna el sonido específico del perro."""
        return "Woof"


class Cat(Animal):
    """Representa a un gato, heredando de Animal."""

    def speak(self):
        """Retorna el sonido específico del gato."""
        return "Meow"


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    print(dog.speak())
    print(cat.speak())

    animals = [Dog(), Cat(), Dog()]
    for animal in animals:
        print(animal.speak())

    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))
