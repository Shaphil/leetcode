"""
Runtime:            123 ms
Beats:              30.55%
Memory:             27.02 MB
Beats:              5.64%
Submission:         https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1488976992/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #dynamic-programming
Solved By:          #array
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_time = 0
        smallest = prices[0]

        for i, price in enumerate(prices):
            if price < smallest:
                smallest = price

            # Calculate potential profit at each step
            profit = price - smallest
            best_time = max(best_time, profit)

            # Early exit if the smallest element is the last element
            if i == len(prices) - 1:
                return max(best_time, 0)

        return best_time


if __name__ == '__main__':
    prices = [2, 4, 1]
    best = Solution().maxProfit(prices)
    print(best)
