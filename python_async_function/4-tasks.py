#!/usr/bin/env python3

"""4-tasks
Remade wait_n but using task_wait_random
"""

from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates many instances of task_wait_random

    Args:
    n (int): number of instances
    max_delay: maximun number of seconds of delay

    Returns:
    list[float]: sorted list of all delays
    """
    delays = []
    tasks = [task_wait_random(max_delay) for i in range(n)]
    for i in tasks:
        delays.append(await i)

    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
