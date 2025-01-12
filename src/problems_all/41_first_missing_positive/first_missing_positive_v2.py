"""
Runtime:            50 ms
Beats:              41.94%
Memory:             28.94 MB
Beats:              48.92%
Submission:         https://leetcode.com/problems/first-missing-positive/submissions/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #hash-table
Solved By:          #array
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == '__main__':
    nums = [7, 8, 9, 11, 12]
    result = Solution().firstMissingPositive(nums)
    print(result)
