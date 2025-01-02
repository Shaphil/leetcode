"""
Runtime:            4 ms
Beats:              32.53%
Memory:             17.91 MB
Beats:              5.15%
Submission:         https://leetcode.com/problems/maximum-score-after-splitting-a-string/submissions/1495282551/
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #string, #prefix-sum
Solved By:          #prefix-sum
"""


class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = sum(int(c) for c in s)  # Count total ones in the string
        max_score = 0
        zeroes_left = 0
        ones_right = total_ones

        # Iterate from 0 to len(s) - 1 to split into non-empty parts
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeroes_left += 1
            else:
                ones_right -= 1

            # Calculate score for the current split
            max_score = max(max_score, zeroes_left + ones_right)

        return max_score


if __name__ == '__main__':
    s = "011101"
    result = Solution().maxScore(s)
    print(result)
