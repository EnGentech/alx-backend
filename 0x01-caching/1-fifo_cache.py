#!/usr/bin/python3
"""FIFO caching"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """class definition"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """insert into cache_data __dict__"""
        if key and item:
            cache_data_count = len(self.cache_data)

            if cache_data_count >= self.MAX_ITEMS and key not in self.cache_data:
                firstItem = next(iter(self.cache_data.keys()))
                print(f"Discard: {firstItem}")
                self.cache_data.pop(firstItem)
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """retrieve item from storage"""
        return self.cache_data.get(key, None)

# Coded by EnGentech
