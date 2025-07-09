"""
https://leetcode.com/problems/move-zeroes/description/


Runtime:            44 ms
Runtime Beats:      12.86%
Memory:             15.1 MB
Memory Beats:       100.00%
Topics:             #array, #two-pointers
Solved By:          #two-pointers
Submission:         https://leetcode.com/problems/move-zeroes/submissions/319600574/
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


def main():
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)


if __name__ == '__main__':
    main()
