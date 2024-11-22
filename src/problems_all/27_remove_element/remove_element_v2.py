"""
Runtime:    0 ms
Beats:      100.00%
Memory:     16.74 MB
Beats:      6.19%
Submission: https://leetcode.com/problems/remove-element/submissions/773526221/
Topics:     #array, #two-pointers
Solved by:  #two-pointers
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                if i != j:
                    nums[i] = nums[j]
                i += 1

        return i


if __name__ == '__main__':
    s = Solution()

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(s.removeElement(nums, val))
