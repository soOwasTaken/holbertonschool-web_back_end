#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LIFOCache
        """
        super().__init__()
        self.order_of_keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.order_of_keys.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.order_of_keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
