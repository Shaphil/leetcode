"""
Runtime:            1106 ms
Beats:              28.42%
Memory:             29.92 MB
Beats:              40.59%
Submission:         https://leetcode.com/problems/minimum-time-to-complete-trips/submissions/1471119377/
Time complexity:    O(n * log(m)), where, n = len(time) and m = totalTrips * max(time)
Space Complexity:   O(1)
Topics:             #array, #binary-search
Solved By:          #binary-search
"""

from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def can_complete_trips(t):
            trips_completed = 0
            for bus_time in time:
                trips_completed += t // bus_time

            return trips_completed >= totalTrips

        left = 1
        right = totalTrips * max(time)

        while left < right:
            mid = left + (right - left) // 2
            if can_complete_trips(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    time = [1, 2, 3]
    totalTrips = 5
    result = Solution().minimumTime(time, totalTrips)
    print(result)
