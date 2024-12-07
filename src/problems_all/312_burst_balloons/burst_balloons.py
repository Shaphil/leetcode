"""
Runtime:            2705 ms
Beats:              80.89%
Memory:             19.19 MB
Beats:              66.20%
Submission:         https://leetcode.com/problems/burst-balloons/submissions/1472785630/
Time complexity:    O(n^3)
Space complexity:   O(n^2)
Topics:             #array, #dynamic-programming
Solved By:          #dynamic-programming
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add virtual balloons with value 1 at the boundaries
        nums = [1] + nums + [1]
        n = len(nums)

        # dp[i][j] represents the maximum coins you can collect by bursting all balloons in the range (i, j)
        dp = [[0] * n for _ in range(n)]

        # Length of the range we are solving
        for length in range(2, n):  # Start from length 2 because we need at least one balloon between (i, j)
            for i in range(n - length):  # Starting index of the range
                j = i + length  # Ending index of the range

                # Iterate through all possible balloons to burst last in the range (i, j)
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
                    )

        # The result is stored in dp[0][n-1], which covers the full range
        return dp[0][n - 1]


if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    result = Solution().maxCoins(nums)
    print(result)
