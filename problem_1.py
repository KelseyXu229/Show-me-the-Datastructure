# -*- coding: utf-8 -*-

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self._size = capacity
        self._cache = {}
        self._keys = []


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self._cache:
            self._keys.remove(key)
            self._keys.insert(0,key)
            return self._cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self._cache:
            self._keys.remove(key)
            self._keys.insert(0,key)
            self._cache[key] = value
        elif len(self._keys) == self._size:
            last = self._keys.pop()
            self._cache.pop(last)
            self._keys.insert(0,key)
            self._cache[key] = value
        else:
            self._keys.insert(0,key)
            self._cache[key] = value

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))     # returns 1
print(our_cache.get(2))     # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry