"""
Runtime:            604 ms
Beats:              5.09%
Memory:             61.81 MB
Beats:              11.23%
Submission:         https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1474475949/
Time complexity:    Insert: O(1), O(n) worst case; Remove: O(1), O(n) worst case; getRandom: O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #math, #design, #randomized
Solved By:          #hash-table
"""

from random import choice


class RandomizedSet:

    def __init__(self):
        self._set = {}

    def insert(self, val: int) -> bool:
        return_val = False
        if not self._set.get(val, False):
            self._set[val] = True
            return_val = True

        return return_val

    def remove(self, val: int) -> bool:
        return_val = False
        if self._set.get(val, False):
            del self._set[val]
            return_val = True

        return return_val

    def getRandom(self) -> int:
        return choice(list(self._set.keys()))


if __name__ == '__main__':
    randomizedSet = RandomizedSet()
    randomizedSet.insert(1)
    randomizedSet.remove(2)
    randomizedSet.insert(2)
    randomizedSet.getRandom()
    randomizedSet.remove(1)
    randomizedSet.insert(2)
    randomizedSet.getRandom()
