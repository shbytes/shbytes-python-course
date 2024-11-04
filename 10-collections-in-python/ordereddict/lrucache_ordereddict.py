from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):    # LRUCache constructor with capacity
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark key as recently used
        return self.cache[key]       # Return value for key

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used item

cache = LRUCache(2)
cache.put(1, "One")
cache.put(2, "Two")  # Elements order => {1: "One", 2: "Two"}
print(cache.get(1))  # Output => One
# With get, key 1 was move to the last position. Key 2 is now at the first position
# Elements order => {2: "Two", 1: "One"}
cache.put(3, "Three") # Cache capacity is 2, first element to be removed to add new element
# Element with key removed from dictionary
# Elements order => {1: "One", 3: "Three"}
print(cache.get(2))  # Output => -1 (removed as least recently used)
