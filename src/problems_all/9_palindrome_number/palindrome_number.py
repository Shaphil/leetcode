"""
Runtime:            71 ms
Beats:              5.22%
Memory:             13.80 MB
Beats:              100.00%
Submission:         https://leetcode.com/problems/palindrome-number/submissions/772722437/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #math
Solved By:          #math
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        inv = ''.join(reversed(s))

        return s == inv


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(100))
