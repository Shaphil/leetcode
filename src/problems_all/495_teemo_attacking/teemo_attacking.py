"""
Runtime:            20 ms
Beats:              49.05%
Memory:             18.65 MB
Beats:              33.85%
Submission:         https://leetcode.com/problems/teemo-attacking/submissions/1503154973/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #simulation
Solved By:          #simulation
"""

from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:  # Handle empty input case
            return 0

        total_duration = 0
        for i in range(len(timeSeries) - 1):
            # Add the minimum of the time until the next attack or the full duration
            total_duration += min(timeSeries[i + 1] - timeSeries[i], duration)

        # Add the duration of the last attack
        total_duration += duration

        return total_duration


if __name__ == '__main__':
    timeSeries = [1, 2]
    duration = 2
    result = Solution().findPoisonedDuration(timeSeries, duration)
    print(result)
