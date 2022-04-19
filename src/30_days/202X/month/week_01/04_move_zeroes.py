"""
https://www.geeksforgeeks.org/move-zeroes-end-array/
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1

        while count < len(nums):
            nums[count] = 0
            count += 1


if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    Solution().moveZeroes(arr)
    print(arr)
