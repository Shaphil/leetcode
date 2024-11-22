"""
Runtime:    3 ms
Beats:      49.91%
Memory:     17.98 MB
Beats:      49.35%
Submission: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1460119994/
Topics:     #array, #two-pointers
Solved by:  #two-pointers
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = Solution().removeDuplicates(nums)
    print(result)
