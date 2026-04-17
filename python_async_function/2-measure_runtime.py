#!/usr/bin/env python3

"""2-measure_runtime
Measure the time of async calls
"""

import asyncio
from time import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the total time of runtime of a async function

    Args:
    n (int): number of instances to run
    max_delay: max delay of each instance

    Returns:
    float: total time of delay divided by the number of instances
    """
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    total_time = end - start

    return total_time / n
