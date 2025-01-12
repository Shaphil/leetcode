"""
Runtime:            30 ms
Beats:              73.81%
Memory:             34.72 MB
Beats:              9.33%
Submission:         https://leetcode.com/problems/first-missing-positive/submissions/1506384109/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table
Solved By:          #hash-set
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num > 0:
                seen.add(num)

        for i in range(1, len(seen) + 2):
            if i not in seen:
                return i

        return len(seen) + 1


if __name__ == '__main__':
    nums = [7, 8, 9, 11, 12]
    result = Solution().firstMissingPositive(nums)
    print(result)
