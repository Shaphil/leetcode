"""
Runtime:            28 ms
Beats:              94.47%
Memory:             14.19 MB
Beats:              100.00%
Submission:         https://leetcode.com/problems/reverse-integer/submissions/572679883/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #math
Solved By:          #math
"""


class Solution:
    def reverse(self, x: int) -> int:
        min_val = -2 ** 31
        max_val = 2 ** 31 - 1
        is_negative = False
        return_val = 0

        if x < 0:
            is_negative = True
            x *= -1

        x = str(x)
        x = reversed(x)
        x = ''.join(list(x))
        x = int(x)

        if is_negative:
            x *= -1

        if x >= min_val and x <= max_val:
            return_val = x

        return return_val


if __name__ == '__main__':
    x = 120
    solution = Solution()
    print(solution.reverse(x))
