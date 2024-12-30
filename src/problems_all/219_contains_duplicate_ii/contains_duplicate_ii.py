"""
Runtime:            20 ms
Beats:              63.81%
Memory:             30.82 MB
Beats:              12.68%
Submission:         https://leetcode.com/problems/contains-duplicate-ii/submissions/1492578036/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #hash-table, #sliding-window
Solved By:          #hash-table
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = dict()

        for i, num in enumerate(nums):
            if num in mapping and i - mapping[num] <= k:
                return True
            mapping[num] = i

        return False


if __name__ == '__main__':
    nums = [1, 0, 1, 1]
    k = 1
    result = Solution().containsNearbyDuplicate(nums, k)
    print(result)
