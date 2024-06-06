from typing import List, Callable

import numpy as np

class BloomFilter:
    def __init__(self, size: int, hash_functions: List[Callable[[int], int]]):
        self.size: int = size
        self.hash_functions: Callable[[int], int] = hash_functions
        self.bit_array = [0] * size

    def add(self, key: int):
        for hash_function in self.hash_functions:
            self.bit_array[hash_function(key)] = 1

    def lookup(self, key: int):
        for hash_function in self.hash_functions:
            if self.bit_array[hash_function(key)] == 0:
                return "Nope"
        return "Probably"
    
    def __str__(self):
        return str(self.bit_array)
    
    def as_register_string(self):
        arr = np.array([range(self.size),self.bit_array])
        return str(arr)