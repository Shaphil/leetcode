"""
Runtime:            161 ms
Beats:              33.09%
Memory:             57.37 MB
Beats:              25.02%
Submission:         https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1474475949/
Time complexity:    Insert: O(1), O(n) worst case; Remove: O(1), O(n) worst case; getRandom: O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #math, #design, #randomized
Solved By:          #hash-table
"""

from random import randint


class RandomizedSet:

    def __init__(self):
        self.values = []  # List to store the values
        self.indices = {}  # Dictionary to store value -> index mapping

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        # Add the value to the end of the list and record its index
        self.indices[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        # Find the index of the value to be removed
        index_to_remove = self.indices[val]
        last_value = self.values[-1]

        # Move the last element to the position of the element to remove
        self.values[index_to_remove] = last_value
        self.indices[last_value] = index_to_remove

        # Remove the last element from the list and delete from the dictionary
        self.values.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        # Generate a random index and return the corresponding value
        random_index = randint(0, len(self.values) - 1)
        return self.values[random_index]


if __name__ == '__main__':
    randomizedSet = RandomizedSet()
    randomizedSet.insert(1)
    randomizedSet.remove(2)
    randomizedSet.insert(2)
    randomizedSet.getRandom()
    randomizedSet.remove(1)
    randomizedSet.insert(2)
    randomizedSet.getRandom()
