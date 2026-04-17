#!/usr/bin/env python3

"""
2-measure_runtime:
Measure the runtime of many parallel coroutines
"""

import asyncio
from time import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension 4 times and measure the total runtime

    Returns:
    float: total runtime of the coroutines
    """
    tasks = [async_comprehension() for _ in range(4)]
    start = time()
    await asyncio.gather(*tasks)
    end = time()
    return end - start
