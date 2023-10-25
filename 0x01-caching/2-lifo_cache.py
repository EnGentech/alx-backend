#!/usr/bin/python3
"""LIFO caching"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """class definition"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.track = ''

    def put(self, key, item):
        """insert into cache_data __dict__"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """retrieve item from storage"""
        if key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None

# Coded by EnGentech
