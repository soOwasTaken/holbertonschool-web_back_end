#!/usr/bin/python3
""" BasicCache module """
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class. Inherits from BaseCaching.
        This caching system doesn’t have limit.
    """

    def put(self, key, item):
        """ Put an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
