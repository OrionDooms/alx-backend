#!/usr/bin/python3
from collections import OrderedDict

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")


    def get(self, key):
        if key is None or key in self.cache_data:
            return None
        return self.cache_data[key]
