"""
Runtime:            0 ms
Beats:              100.00%
Memory:             17.87 MB
Beats:              30.22%
Submission:         https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1497808711/
Time complexity:    O(log(min(m, n))), where, `m = len(nums1)` and `n = len(nums2)`
Space complexity:   O(1)
Topics:             #array, #binary-search, #divide-and-conquer
Solved By:          #binary-search
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        lo, hi = 0, x

        while lo <= hi:
            mid_x = (lo + hi) // 2
            mid_y = (x + y + 1) // 2 - mid_x

            max_left_x = float('-inf') if mid_x == 0 else nums1[mid_x - 1]
            max_left_y = float('-inf') if mid_y == 0 else nums2[mid_y - 1]

            min_right_x = float('inf') if mid_x == x else nums1[mid_x]
            min_right_y = float('inf') if mid_y == y else nums2[mid_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > max_left_y:
                hi = mid_x - 1
            else:
                lo = mid_x + 1


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(result)
