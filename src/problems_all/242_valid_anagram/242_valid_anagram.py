"""
https://leetcode.com/problems/valid-anagram/description/

Runtime: 53 ms
Memory: 14.5 MB
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    result = Solution().isAnagram(s, t)
    print(result)
