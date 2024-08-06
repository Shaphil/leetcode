"""
https://leetcode.com/problems/range-sum-query-immutable/description/

Runtime:    62 ms
Memory:     20.2 MB
https://leetcode.com/problems/range-sum-query-immutable/submissions/1347037242/
"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    arr = NumArray(nums)
    res = arr.sumRange(0, 4)
    print(res)
