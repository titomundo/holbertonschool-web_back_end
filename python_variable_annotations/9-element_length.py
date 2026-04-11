#!/usr/bin/env python3

"""9-element_lenght
A function that inputs a iterable of squences and
returns a list of tuples with a sequence and int???
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with a Sequence and an integer

    Args:
    lst (Iterable[Sequence]): Iterable of sequences (?)

    Returns:
    a list of tuples with a Sequence and an integer

    """
    return [(i, len(i)) for i in lst]
