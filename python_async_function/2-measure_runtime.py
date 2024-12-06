#!/usr/bin/env python3
"""Module that contains a 'measure_time' function """


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the execution time for wait_n """

    start_time = time.time() # Log start time
    asyncio.run(wait_n(n, max_delay)) # Execute function
    end_time = time.time() # Log end time

    return end_time - start_time # Return total execution time
