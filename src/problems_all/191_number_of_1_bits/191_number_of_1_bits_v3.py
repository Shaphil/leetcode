"""
https://leetcode.com/problems/number-of-1-bits/description/

Runtime: 34 ms
Memory: 13.9 MB
"""

from collections import Counter


class Solution:
    def hammingWeight(self, n: int) -> int:
        _bin = format(n, 'b')
        digits_count = Counter(_bin)
        return digits_count.get('1', 0)


def main():
    n = 123
    weight = Solution().hammingWeight(n)
    print(weight)


if __name__ == '__main__':
    main()
