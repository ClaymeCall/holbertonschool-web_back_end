#!/usr/bin/env python3
""" Module that contains a 'task_await_random' function """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Return an asyncio.Task object with wait_random function """
    return asyncio.create_task(wait_random(max_delay))
