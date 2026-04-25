#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the values from a range of indexes

        Args:
        page (int): current page
        page_size: number of elements by page

        Returns:
        List[List]: list of fetch values, empty list if out of range parameters
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        idx = index_range(page, page_size)

        return data[idx[0]:idx[1]]
