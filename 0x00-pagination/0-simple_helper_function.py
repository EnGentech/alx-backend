#!/usr/bin/env python3
"""
Author: Iberedem Inyang
Description: This code is written with two parameters of a function
to return an index corresponding to the user input
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    This function is defined to fine the start and end pagination
    of a page based on the page_size multiplied by the start index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
