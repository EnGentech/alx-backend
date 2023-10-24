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
        """insert into cache_data __dict__
        whit poping the last if list exceeds limit
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(True)
            print("DISCARD:", first_key)

    def get(self, key):
        """retrieve item from storage"""
        if key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None

# Coded by EnGentech
