"""
Runtime:    49 ms
Beats:      5.75%
Memory:     13.79 MB
Beats:      100.00%
https://leetcode.com/problems/remove-element/submissions/773526221/
Topics:     #array, #two-pointers
Solved by:  #two-pointers
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


if __name__ == '__main__':
    s = Solution()

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(s.removeElement(nums, val))

    nums = [3, 2, 2, 3]
    val = 3
    print(s.removeElement(nums, val))
