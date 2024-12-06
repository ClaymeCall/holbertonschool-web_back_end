#!/usr/bin/env python3
""" Module that contains a 'to_kv' function """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple of its arguments and squares the second one """
    return (k, v ** 2)
