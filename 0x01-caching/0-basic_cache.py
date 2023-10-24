#!/usr/bin/python3
"""Basic caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class definition"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """insert into cache_data __dict__"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """retrieve item from storage"""
        return self.cache_data.get(key, None)

# Coded by EnGentech
