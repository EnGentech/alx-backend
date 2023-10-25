#!/usr/bin/python3
"""LIFO caching"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """class definition"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.track = []

    def put(self, key, item):
        """insert into cache_data __dict__"""
        cache_data_count = len(self.cache_data)

        if key and item:
            if cache_data_count >= self.MAX_ITEMS \
                    and key not in self.cache_data:
                firstKey, _ = self.cache_data.popitem(True)
                print(f"Discard: {firstKey}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """retrieve item from storage"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data.get(key)
        else:
            return None

# Coded by EnGentech
