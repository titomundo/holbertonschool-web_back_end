#!/usr/bin/env python3

"""
0-async_comprehension
Use async comprehension to extract values to iterables
"""

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """
    Gets 10 random numbers using async_generator

    Returns:
    list: 10 random numbers from 0 to 10
    """

    result = []
    async for i in async_generator():
        result.append(i)

    return result
