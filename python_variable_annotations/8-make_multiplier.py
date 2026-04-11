#!/usr/bin/env python3

"""8-make_multiplier
Create a function that returns a callable function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier

    Args:
    multiplier (float): multiplier

    Returns:
    Callable[[float], float]: function that multiplies by multiplier
    """
    return lambda x: x * multiplier
