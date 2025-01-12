"""
Runtime:            21 ms
Beats:              81.49%
Memory:             31.34 MB
Beats:              33.33%
Submission:         https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/1506297041/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #hash-table
Solved By:          #hash-set
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in n:
                res.append(i)

        return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = Solution().findDisappearedNumbers(nums)
    print(result)
