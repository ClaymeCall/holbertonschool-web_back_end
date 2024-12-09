#!/usr/bin/env python3
""" Module that contains a 'async_generator' function """

import random
import asyncio

async def async_generator():
    """ Yields 10 random numbers after waiting 1 sec for each """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0,10)
