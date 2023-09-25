#!/usr/bin/python3
""" LIFOCache module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class. Inherits from BaseCaching.
        Uses LIFO algorithm.
    """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Put an item in the cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if key not in self.stack:
            self.stack.append(key)

        if len(self.stack) > BaseCaching.MAX_ITEMS:
            discarded_key = self.stack.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
