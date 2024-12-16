"""
Runtime:            0 ms
Beats:              100.00%
Memory:             17.48 MB
Beats:              6.61%
Submission:         https://leetcode.com/problems/palindrome-number/submissions/1480378948/
Time complexity:    O(log10 n)
Space complexity:   O(1)
Topics:             #math
Solved By:          #math
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False  # Negative numbers and numbers ending in 0 (except 0) are not palindromes

        # Reverse half of the number efficiently
        rev = 0
        while x > rev:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        # Compare the original and reversed halves
        return x == rev or x == rev // 10  # Handle odd and even number of digits


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(100))
