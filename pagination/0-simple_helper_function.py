#!/usr/bin/env python3

"""
0-simple_helper_function:
Helper function to convert a range of numbers into a tuple
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple of a start and end index
    corresponding to pagination parameters

    Args;
    page (int): current page
    page_size: number of elements by page

    Returns:
    Tuple: the starting and ending index or the range

    """
    size = page * page_size
    return (size - page_size, size)
