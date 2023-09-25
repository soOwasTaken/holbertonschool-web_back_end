#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LRUCache
        """
        super().__init__()
        self.order_of_keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order_of_keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_used_key = self.order_of_keys.pop(0)
            del self.cache_data[least_used_key]
            print(f"DISCARD: {least_used_key}")

        self.cache_data[key] = item
        self.order_of_keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.order_of_keys.remove(key)
        self.order_of_keys.append(key)
        return self.cache_data.get(key)
