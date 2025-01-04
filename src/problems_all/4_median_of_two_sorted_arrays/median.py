"""
Runtime:            0 ms
Beats:              100.00%
Memory:             17.93 MB
Beats:              24.25%
Submission:         https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1497612898/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #array, #binary-search, #divide-and-conquer
Solved By:          #array
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        total = len(merged)

        if total % 2 == 1:
            return float(merged[total // 2])
        else:
            mid1 = merged[total // 2 - 1]
            mid2 = merged[total // 2]
            return (float(mid1) + float(mid2)) / 2.0


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(result)
