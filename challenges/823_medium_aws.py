"""
Implement a bit array.
A bit array is a space efficient array that holds a value of 1 or 0 at each index.
* init(size): initialize the array with size
* set(i, val): updates index at i with val where val is either 1 or 0.
* get(i): gets the value at index i.
"""

class BitArray:
    def __init__(self, size: int):
        self.size = size
        self.array = []
        for i in size:
            self.array.append(None)

    def set(self, i: int, val: int):
        if i > self.size:
            print('The index range of the actual bit array is less than {}'.format(i))
        if val not in [0,1]:
            print('The index range of the actual bit array is less than {}'.format(i))



