"""
Runtime:            7 ms
Beats:              74.56%
Memory:             21.78 MB
Beats:              5.12%
Submission:         https://leetcode.com/problems/merge-intervals/submissions/1500847482/
Time complexity:    O(n log n)
Space complexity:   O(n)
Topics:             #array, #sorting
Solved By:          #sorting
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals based on their start times
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]  # Initialize with the first interval

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:  # Check for overlap with the previous interval
                merged[-1][1] = max(merged[-1][1], end)  # Merge the intervals
            else:
                merged.append([start, end])  # Add a new non-overlapping interval

        return merged


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = Solution().merge(intervals)
    print(result)
