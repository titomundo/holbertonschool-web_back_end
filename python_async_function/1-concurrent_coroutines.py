#!/usr/bin/env python3

"""1-concurrent_coroutines
Create many async calls
"""

from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates many instances of wait_random

    Args:
    n (int): number of instances
    max_delay: maximun number of seconds of delay
    Returns:
    list[float]: sorted list of all delays
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)

    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
