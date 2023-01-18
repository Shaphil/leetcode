"""
https://leetcode.com/problems/find-the-difference/

Runtime: 40 ms
Memory: 13.8 MB
https://leetcode.com/problems/find-the-difference/submissions/880557739/
"""

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = Counter(t) - Counter(s)
        return x.popitem()[0]


def main():
    s = "ae"
    t = "aea"
    result = Solution().findTheDifference(s, t)
    print(result)


if __name__ == '__main__':
    main()
