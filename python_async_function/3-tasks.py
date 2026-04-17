#!/usr/bin/env python3

"""3-tasks
Creates an async task without using async
"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Schedules a coroutine object from wait_random()

    Args:
    max_delay (int): max delay for wait_random

    Returns:
    asyncio.Task: Async coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
