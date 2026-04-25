#!/usr/bin/env python3

"""
2-hypermedia_pagination:
Get a range of entries from a dataset using pagination
and information about the paginated dataset
"""

import csv
import math
from typing import Dict, List, Tuple


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a collection of infrormation about a paginated dataset

        Args:
        page (int): current page
        page_size: number of elements by page

        Returns:
        Dict: list of fetch values with information about pages, page size, etc
        """
        plen = len(self.dataset())
        data = self.get_page(page, page_size)
        next_page = None
        prev_page = None
        total_pages = math.ceil(plen / page_size)

        if page + 1 < total_pages:
            next_page = page + 1

        if page - 1 > 0:
            prev_page = page - 1

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
