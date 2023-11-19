"""
Data module for Morse code conversion.

This module defines dictionaries for mapping letters and numbers to their
respective Morse code representations. These dictionaries are used by the
main application for converting text input into Morse code.

Attributes:
    LETTERS (dict): A dictionary mapping uppercase letters and space to their
        Morse code representations.
    NUMBERS (dict): A dictionary mapping numeric digits to their Morse code
        representations.
"""

LETTERS = {'A' : "•-",
           'B' : "-•••",
           'C' : "-•-•",
           'D' : "-••",
           'E' : "•",
           'F' : "••-•",
           'G' : "--•",
           'H' : "••••",
           'I' : "••",
           'J' : "•---",
           'K' : "-•-",
           'L' : "•-••",
           'M' : "--",
           'N' : "-•",
           'O' : "---",
           'P' : "•--•",
           'Q' : "--•-",
           'R' : "•-•",
           'S' : "•••",
           'T' : "-",
           'U' : "••-",
           'V' : "•••-",
           'W' : "•--",
           'X' : "-••-",
           'Y' : "-•--",
           'Z' : "--••",
           ' ' : ""}

NUMBERS = {'1' : "•----",
           '2' : "••---",
           '3' : "•••--",
           '4' : "••••-",
           '5' : "•••••",
           '6' : "-••••",
           '7' : "--•••",
           '8' : "---••",
           '9' : "----•",
           '0' : "-----",}