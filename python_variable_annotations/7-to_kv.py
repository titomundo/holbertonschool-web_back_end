#!/usr/bin/env python3

"""7-to_kv
Create a tuple from a string and an int OR float"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple created from a string and an int OR float

    Args:
    k (str): string of the tuple
    v (int | float): number to square

    Returns:
    tuple[str, float]
    """
    return (k, float(v**2))
