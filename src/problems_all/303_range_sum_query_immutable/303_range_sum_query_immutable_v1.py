"""
https://leetcode.com/problems/range-sum-query-immutable/description/

Runtime: 1100 ms
Memory: 17.5 MB
https://leetcode.com/problems/range-sum-query-immutable/submissions/539366974/
"""


from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
