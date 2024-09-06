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
        if key is not None or item is not None:
            self.cache_data[key] = item
            if BaseCaching.MAX_ITEMS < len(self.cache_data):
                first_key, _ = self.cache_data.popitem(False)
                print("DISCARD: {}".format(first_key))
            else:
                return
        else:
            return

    def get(self, key):
        """if key is None or key not in self.cache_data:
            return None"""
        return self.cache_data(key)
