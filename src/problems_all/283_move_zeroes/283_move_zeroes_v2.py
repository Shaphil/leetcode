"""
Runtime:            4 ms
Beats:              61.77%
Memory:             18.70 MB
Beats:              78.99%
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #two-pointers
Solved By:          #two-pointers
Submission:         https://leetcode.com/problems/move-zeroes/submissions/1692193930/
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


def main():
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)


if __name__ == '__main__':
    main()
