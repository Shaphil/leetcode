"""
Runtime:            47 ms
Beats:              85.53%
Memory:             28.25 MB
Beats:              33.65%
Submission:         https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1474475949/
Time complexity:    O(n log k),
Space complexity:   O(k)
Topics:             #array, #divide-and-conquer, #sorting, #heap #priority-queue, #quickselect
Solved By:          #heap
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use a min-heap of size k
        heap = nums[:k]
        heapq.heapify(heap)  # Build the heap, O(k)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)  # Replace smallest if num is larger, O(log k)

        return heap[0]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = Solution().findKthLargest(nums, k)
    print(result)
