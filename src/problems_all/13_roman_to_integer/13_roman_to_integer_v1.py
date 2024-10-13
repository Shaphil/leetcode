"""
Runtime:    35 ms
RT Beats:   96.44%
Memory:     16.66 MB
Mem Beats:  14.59%
Submission: https://leetcode.com/problems/roman-to-integer/submissions/1421066124/
"""

ROMAN_TO_INT = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prev_value = 0

        for char in s:
            current_value = ROMAN_TO_INT[char]
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value

        return total


if __name__ == '__main__':
    solution = Solution()
    s = "MCMXCIV"
    result = solution.romanToInt(s)
    print(result)
