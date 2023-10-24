#!/usr/bin/python3
"""Basic caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class definition"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """insert into cache_data __dict__"""
        self.cache_data[key] = item

    def get(self, key):
        """retrieve item from storage"""
        if key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None

# Coded by EnGentech
