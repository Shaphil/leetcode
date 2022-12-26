"""
https://leetcode.com/problems/number-of-1-bits/description/

Runtime: 31 ms
Memory: 13.9 MB
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        _bin = format(n, 'b')
        digits = list(_bin)
        return digits.count('1')


def main():
    n = 123
    weight = Solution().hammingWeight(n)
    print(weight)


if __name__ == '__main__':
    main()
