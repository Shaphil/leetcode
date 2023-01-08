"""
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

O(1)
Runtime: 34 ms
Memory: 13.9 MB
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/submissions/865170025/
"""


class Solution:
    """
    The number of odd numbers between 0 and n is n // 2 where n is even
    So we promote `high` to the next even number and downgrade low to 
    the previous even number.

    1. we calculate how many odds are there between 0 - high
    2. we calculate the number of odds between 0- low
    3. the difference between these two odds is the result
    """

    def countOdds(self, low: int, high: int) -> int:
        hi_odds = high // 2 if high % 2 == 0 else (high + 1) // 2
        lo_odds = low // 2 if low % 2 == 0 else (low - 1) // 2
        return hi_odds - lo_odds


def main():
    low = 1
    high = 13
    odds = Solution().countOdds(low, high)
    print(odds)


if __name__ == '__main__':
    main()
