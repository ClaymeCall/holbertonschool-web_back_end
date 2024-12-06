#!/usr/bin/env python3
"""Module that contains a 'wait_n' function """


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    task_list = [wait_random(max_delay) for i in range(n)]
    results = []

    for task in asyncio.as_completed(task_list):
        results.append(await task)

    return results
