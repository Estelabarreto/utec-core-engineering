#!/usr/bin/env python3
"""
Module that provides a function to read and print text files.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
