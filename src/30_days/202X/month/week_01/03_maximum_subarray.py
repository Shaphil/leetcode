"""
https://youtu.be/2MmGzdiKR9Y
https://backtobackswe.com/platform/content/max-contiguous-subarray-sum/solutions
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = -2147483648
        current = 0

        for i in nums:
            current += i
            best = max(best, current)
            current = max(0, current)
            print(f'i: {i}, current: {current}, best: {best}')

        return best


if __name__ == "__main__":
    arr = [-2, -1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    top = solution.maxSubArray(arr)
    print(top)
