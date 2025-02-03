"""
Runtime:            0 ms
Beats:              100.00%
Memory:             17.91 MB
Beats:              11.65%
Submission:         https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/submissions/1529986517/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array
Solved By:          #array
"""
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 1
        increasing = 1
        decreasing = 1

        if n == 1:
            return 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increasing += 1
                decreasing = 1
            elif nums[i] < nums[i - 1]:
                decreasing += 1
                increasing = 1
            else:
                increasing = 1
                decreasing = 1

            longest = max(longest, increasing, decreasing)

        return longest


if __name__ == '__main__':
    nums = [1, 4, 3, 3, 2]
    result = Solution().longestMonotonicSubarray(nums)
    print(result)
