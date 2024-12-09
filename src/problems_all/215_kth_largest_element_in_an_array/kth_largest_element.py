"""
Runtime:            71 ms
Beats:              59.43%
Memory:             14.65 MB
Beats:              100.00%
Submission:         https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/728442198/
Time complexity:    O(n log n)
Space complexity:   O(n)
Topics:             #array, #divide-and-conquer, #sorting, #heap #priority-queue, #quickselect
Solved By:          #sorting
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rev_sorted = sorted(nums, reverse=True)
        return rev_sorted[k - 1]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = Solution().findKthLargest(nums, k)
    print(result)
