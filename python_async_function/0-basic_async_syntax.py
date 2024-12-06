#!/usr/bin/env python3
"""Module that contains a 'wait_random' function """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay up to a max_delay arg
    and returns the delay value"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
