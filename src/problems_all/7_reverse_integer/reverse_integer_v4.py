"""
Runtime:            32 ms
Beats:              82.67%
Memory:             17.92 MB
Beats:              5.74%
Submission:         https://leetcode.com/problems/reverse-integer/submissions/1485575754/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #math
Solved By:          #math
"""


class Solution:
    def reverse(self, x: int) -> int:
        min_val = -2 ** 31
        max_val = 2 ** 31 - 1

        # Reverse the integer as a string and handle sign
        reversed_x = int(str(abs(x))[::-1])
        if x < 0:
            reversed_x = -reversed_x

        # Check for overflow
        if reversed_x < min_val or reversed_x > max_val:
            return 0
        return reversed_x



if __name__ == '__main__':
    x = -120
    solution = Solution()
    print(solution.reverse(x))
