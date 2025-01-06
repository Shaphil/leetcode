"""
Runtime:            78 ms
Beats:              15.03%
Memory:             30.01 MB
Beats:              31.54%
Submission:         https://leetcode.com/problems/find-the-duplicate-number/submissions/1499698833/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #two-pointers, #binary-search, #bit-manipulation
Solved By:          #two-pointers
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    result = Solution().findDuplicate(nums)
    print(result)
