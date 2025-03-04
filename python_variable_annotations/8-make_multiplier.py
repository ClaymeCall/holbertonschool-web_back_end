#!/usr/bin/env python3
""" Module that contains a 'make_multiplier' function """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a number by a given multiplier"""

    def multiply(n: float) -> float:
        """ Multiplies a number by a given multiplier"""
        return n * multiplier

    return multiply
