#!/usr/bin/python3
"""LRU Caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching"""
    def __init___(self):
        """Initialize with object attributes, super() inherit attributes
        from parent class and the OrderedDict class and assign it to the
        self.cache_data attribute"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the items value
        for the key"""
        if key is not None or item is not None:
            if key in self.cache_data:
                self.cache_order.remove(key)
                """self.cashe_order: keep track of the order of items added
                to the cache"""
                self.cache_data[key] = item
                self.access_order.append(key)
                if BaseCaching.MAX_ITEMS < len(self.cache_data):
                    last = self.access_order.pop()
                    del sel.cache_data[last]
                    print("DISCARD:".format(last))
            else:
                return
        else:
            return

    def get(self, key):
        """ Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None."""
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
