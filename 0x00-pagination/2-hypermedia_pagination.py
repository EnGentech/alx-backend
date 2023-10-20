#!/usr/bin/env python3
"""
Author: Iberedem Inyang
Description: This code is written with two parameters of a function
to return an index corresponding to the user input
"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    This function is defined to fine the start and end pagination
    of a page based on the page_size multiplied by the start index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        we will get to this later
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        return self.dataset()[start: end]

    def get_hyper(self, page: int = 0, page_size: int = 0) -> List[List]:
        """
        document statistics
        """
        total_pages = round(len(self.dataset()) / page_size)
        previous_page = None if page - 1 <= 0 else page - 1
        next_page = None if page + 1 > total_pages else page + 1
        data = self.get_page(page, page_size)
        
        stat = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'previous_page': previous_page,
            'total_pages': total_pages
        }
        return stat