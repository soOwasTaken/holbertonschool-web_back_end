#!/usr/bin/python3
""" FIFOCache module """
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """ FIFOCache class. Inherits from BaseCaching.
        Uses FIFO algorithm.
    """

    def __init__(self):
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """ Put an item in the cache """
        if key is None or item is None:
            return

        if key not in self.keys:
            self.keys.append(key)

        self.cache_data[key] = item

        if len(self.keys) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.popleft()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
