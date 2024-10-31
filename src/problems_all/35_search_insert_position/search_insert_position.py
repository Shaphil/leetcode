"""
Runtime:    0 ms
Beats:      100.00%
Memory:     17.30 MB
Beats:      60.46%
Submission: https://leetcode.com/problems/search-insert-position/submissions/1439152588/
"""

from typing import List


class Solution:
    def binary_search(self, arr, lo, hi, x):
        if hi >= lo:
            mid = (hi + lo) // 2

            if arr[mid] == x:
                return mid

            elif arr[mid] > x:
                return self.binary_search(arr, lo, mid - 1, x)

            else:
                return self.binary_search(arr, mid + 1, hi, x)

        else:
            return -1

    def searchInsert(self, nums: List[int], target: int) -> int:
        res = self.binary_search(nums, 0, len(nums) - 1, target)
        if res != -1:
            return res

        else:
            for i, v in enumerate(nums):
                if v > target:
                    return i

            return len(nums)


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 7
    result = Solution().searchInsert(nums, target)
    print(result)
