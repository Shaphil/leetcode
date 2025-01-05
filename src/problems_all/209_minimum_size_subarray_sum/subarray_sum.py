"""
Runtime:            7 ms
Beats:              93.12%
Memory:             28.35 MB
Beats:              12.24%
Submission:         https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1498576208/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #binary-search, #sliding-window, #prefix-sum
Solved By:          #sliding-window
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = float('inf')
        current_sum = 0
        start = 0

        for end in range(n):
            current_sum += nums[end]

            # Shrink the window as long as the sum is >= target
            while current_sum >= target:
                min_length = min(min_length, end - start + 1)
                current_sum -= nums[start]
                start += 1

        return min_length if min_length != float('inf') else 0


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    result = Solution().minSubArrayLen(target, nums)
    print(result)
