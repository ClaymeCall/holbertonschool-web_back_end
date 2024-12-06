#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
""" Module that contains a 'element_length' function"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples of elements and their length """
    return [(i, len(i)) for i in lst]
