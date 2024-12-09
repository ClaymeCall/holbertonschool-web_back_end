#!/usr/bin/env python3
""" Module that contains a 'async_comprehension' function """

from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ Returns the results of a generator in a list """
    return [item async for item in async_generator()]
