#!/usr/bin/env python3
"""Module that contains a 'task_wait_n' function """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Return an asyncio.Task object with wait_random function """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of delays of multiple wait_random coroutines """
    task_list = [wait_random(max_delay) for i in range(n)]

    return [await delay for delay in asyncio.as_completed(task_list)]
