"""
Runtime:    0 ms
Beats:      100.00%
Memory:     16.56 MB
Beats:      72.19%
Submission: https://leetcode.com/problems/length-of-last-word/submissions/1440795215/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sentence = s.strip().split(' ')
        if len(sentence) > 0:
            return len(sentence[-1])

        return 0


if __name__ == '__main__':
    s = "Hello World"
    solution = Solution()
    result = solution.lengthOfLastWord(s)
    print(result)
