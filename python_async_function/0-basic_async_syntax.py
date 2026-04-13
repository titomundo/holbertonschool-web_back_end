#!/usr/bin/env python3

import asyncio
from random import uniform

"""0-basic_async_syntax:
Demostration of an async function using sleep"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Sleeps for a random number between 0 and
    max_delay before returning the delay value

    Args:
    max_delay (int = 10): upper limit for the delay

    Returns:
    float: delay value generated randomly using max_delay
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
