"""
Runtime:            63 ms
Beats:              7.30%
Memory:             13.85 MB
Beats:              100.00%
Submission:         https://leetcode.com/problems/reverse-integer/submissions/572679883/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #math
Solved By:          #math
"""


class Solution:
    def reverse(self, x: int) -> int:
        hi = 2 ** 31 - 1
        lo = -2 ** 31

        is_neg = False
        if x < 0:
            x *= -1
            is_neg = True

        s = list(str(x))
        s.reverse()
        r = int(''.join(s))

        if r > hi or r < lo:
            r = 0

        if is_neg:
            r *= -1

        return r


def solve():
    x = 120
    solution = Solution()
    print(solution.reverse(x))


if __name__ == '__main__':
    solve()
