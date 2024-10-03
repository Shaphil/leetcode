"""
Runtime:    186 ms
Memory:     14.23 MB
Submission: https://leetcode.com/problems/count-the-number-of-consistent-strings/submissions/1410391521/
"""

from collections import Counter


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_counter = Counter(allowed)
        total = 0

        for word in words:
            for char in word:
                if char not in allowed_counter:
                    break
            else:
                total += 1

        return total


if __name__ == '__main__':
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    solution = Solution().countConsistentStrings(allowed, words)
    print(solution)
