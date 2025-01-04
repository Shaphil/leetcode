"""
Runtime:            0 ms
Beats:              100.00%
Memory:             18.75 MB
Beats:              17.44%
Submission:         https://leetcode.com/problems/missing-number/submissions/1497563813/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #hash-table, #math, #binary-search, #bit-manipulation, #sorting
Solved By:          #math
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = (n * (n + 1)) // 2
        actual = sum(nums)
        return expected - actual


if __name__ == '__main__':
    nums = [3, 0, 1]
    result = Solution().missingNumber(nums)
    print(result)
