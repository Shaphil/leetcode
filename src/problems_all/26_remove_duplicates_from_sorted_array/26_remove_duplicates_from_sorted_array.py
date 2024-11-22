"""
Runtime:    83 ms
Beats:      5.05%
Memory:     15.61 MB
Beats:      100.00%
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[current] = nums[i + 1]
                current += 1

        return current


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = Solution().removeDuplicates(nums)
    print(result)
