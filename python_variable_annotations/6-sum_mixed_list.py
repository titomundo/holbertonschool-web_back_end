#!/usr/bin/env python3

"""6-sum_mixed
Return the sum of a mixed bag of numbers"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of floats and integers

    Args:
    input_list (list[float | int]): list of numbers

    Returns:
    float: Sum of floats
    """
    return sum(mxd_list)
