"""
https://www.geeksforgeeks.org/stock-buy-sell/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        n = len(prices)

        while i < n - 1:
            while (i < (n - 1)) and (prices[i + 1] <= prices[i]):
                i += 1

            if i == n - 1:
                break

            buy = prices[i]
            i += 1

            while (i < n) and (prices[i] >= prices[i - 1]):
                i += 1

            sell = prices[i - 1]
            current = sell - buy
            profit += current

        return profit


if __name__ == "__main__":
    stock = [7, 1, 5, 3, 6, 4]
    profit = Solution().maxProfit(stock)
    print(profit)
