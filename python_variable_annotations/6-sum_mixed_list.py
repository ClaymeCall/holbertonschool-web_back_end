#!/usr/bin/env python3
""" Module that contains a 'sum_mixed_list' function """


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of a list of int/float as float """
    return sum(mxd_lst)
