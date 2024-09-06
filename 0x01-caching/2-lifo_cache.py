#!/usr/bin/python3
"""LIFO Caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching"""
    def __init__(self):
        """Initialize with object attributes, super() inherit attributes
        from parent class and the OrderedDict class and assign it to the
        self.cache_data attribute"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the items value
        for the key"""
        if key is not None or item is not None:
            if key not in self.cache_data:
                if BaseCaching.MAX_ITEMS <= len(self.cache_data):
                    last_key = next(reversed(self.cache_data))
                    print("DISCARD: {}".format(last_key))
                    del self.cache_data[last_key]
                self.cache_data[key] = item
            else:
                return
        else:
            return

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
