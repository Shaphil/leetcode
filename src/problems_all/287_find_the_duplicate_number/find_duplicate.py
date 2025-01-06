"""
Runtime:            78 ms
Beats:              15.03%
Memory:             30.01 MB
Beats:              31.54%
Submission:         https://leetcode.com/problems/find-the-duplicate-number/submissions/1499684006/
Time complexity:    O(n log n)
Space complexity:   O(1)
Topics:             #array, #two-pointers, #binary-search, #bit-manipulation
Solved By:          #two-pointers
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        current = nums[0]
        prev = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]
            if prev == current:
                return current

            prev = current


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    result = Solution().findDuplicate(nums)
    print(result)
