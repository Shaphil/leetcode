"""
Runtime:            36 ms
Beats:              60.46%
Memory:             17.98 MB
Beats:              5.74%
Submission:         https://leetcode.com/problems/reverse-integer/submissions/1485571834/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #math
Solved By:          #math
"""


class Solution:
    def reverse(self, x: int) -> int:
        min_val = -2 ** 31
        max_val = 2 ** 31
        reversed_num = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        reversed_num *= sign
        return reversed_num if min_val <= reversed_num <= max_val else 0


if __name__ == '__main__':
    x = -120
    solution = Solution()
    print(solution.reverse(x))
