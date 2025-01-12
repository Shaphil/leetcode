"""
Runtime:            35 ms
Beats:              45.26%
Memory:             40.04 MB
Beats:              6.21%
Submission:         https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/1506278667/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table
Solved By:          #array
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = [n for n in range(1, len(nums) + 1)]
        return list(set(x).difference(set(nums)))


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = Solution().findDisappearedNumbers(nums)
    print(result)
