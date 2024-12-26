"""
Runtime:            30 ms
Beats:              87.40%
Memory:             27.04 MB
Beats:              5.64%
Submission:         https://leetcode.com/problems/word-search/submissions/1477947774/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #array, #dynamic-programming
Solved By:          #array
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


if __name__ == '__main__':
    prices = [2, 4, 1]
    best = Solution().maxProfit(prices)
    print(best)
