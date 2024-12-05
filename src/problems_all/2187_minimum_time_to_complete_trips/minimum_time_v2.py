"""
Runtime:            1018 ms
Beats:              45.47%
Memory:             30.91 MB
Beats:              18.41%
Submission:         https://leetcode.com/problems/minimum-time-to-complete-trips/submissions/1471119377/
Time complexity:    O(n * log(m)), where, n = len(time) and m = totalTrips * max(time)
Space Complexity:   O(1)
Topics:             #array, #binary-search
Solved By:          #binary-search
"""

from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1  # Minimum possible time
        right = max(time) * totalTrips  # Maximum possible time

        while right > left:
            mid = (left + right) // 2  # Calculate the middle point
            sums = sum([mid // t for t in time])  # Calculate the total trips completed in mid time units
            if sums >= totalTrips:  # If the total trips are enough, we can reduce the upper bound
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    time = [1, 2, 3]
    totalTrips = 5
    result = Solution().minimumTime(time, totalTrips)
    print(result)
