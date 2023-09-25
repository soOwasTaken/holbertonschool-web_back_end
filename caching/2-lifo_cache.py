#!/usr/bin/python3
""" LRUCache module """
from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """ LRUCache class. Inherits from BaseCaching.
        Uses LRU algorithm.
    """

    def __init__(self):
        super().__init__()
        self.lru_order = deque()

    def put(self, key, item):
        """ Put an item in the cache """
        if key is None or item is None:
            return

        if key in self.lru_order:
            self.lru_order.remove(key)
        self.lru_order.append(key)

        self.cache_data[key] = item

        if len(self.lru_order) > BaseCaching.MAX_ITEMS:
            discarded_key = self.lru_order.popleft()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Get an item by key """
        value = self.cache_data.get(key, None)
        if value is not None:
            self.lru_order.remove(key)
            self.lru_order.append(key)
        return value
