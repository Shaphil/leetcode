"""
Runtime:            7 ms
Beats:              39.14%
Memory:             19.78 MB
Beats:              6.70%
Submission:         https://leetcode.com/problems/missing-number/submissions/1497554237/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #math, #binary-search, #bit-manipulation, #sorting
Solved By:          #hash-table (#hash-set)
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = set(range(len(nums) + 1))
        missing = expected.difference(set(nums))
        return missing.pop()


if __name__ == '__main__':
    nums = [3, 0, 1]
    result = Solution().missingNumber(nums)
    print(result)
