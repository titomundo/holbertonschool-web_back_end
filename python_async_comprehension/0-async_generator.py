#!/usr/bin/env python3

"""0-async_generator
Create a coroutine that generates random numbers each second
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yields random numbers from 0 to 10 every second
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
