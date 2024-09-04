#!/usr/bin/python3
"""FIFO caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits from BaseCaching"""
    def __init__(self):
        """Initialize with object attributes, super() inherit attributes
        from parent class and the OrderedDict class and assign it to the
        self.cache_data attribute"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the items value
        for the key"""
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first_key = next(iter(self.cache_data))
                    print("DISCARD: {}".format(first_key))
                    self.cache_data.pop(first_key)
            self.cache_data[key] = item

    def get(self, key):
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
