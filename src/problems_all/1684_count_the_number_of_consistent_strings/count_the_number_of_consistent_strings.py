"""
Runtime:    186 ms
Memory:     14.23 MB
Submission: https://leetcode.com/problems/count-the-number-of-consistent-strings/submissions/1410391521/
"""


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        total = 0
        allowed = set(allowed)
        for word in words:
            w = set(word)
            if w.issubset(allowed):
                total += 1

        return total


if __name__ == '__main__':
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    solution = Solution().countConsistentStrings(allowed, words)
    print(solution)
