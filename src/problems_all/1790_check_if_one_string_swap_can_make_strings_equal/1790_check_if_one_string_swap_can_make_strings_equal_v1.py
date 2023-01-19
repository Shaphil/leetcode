"""
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

Runtime: 36 ms
Memory: 13.7 MB
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/submissions/881281776/
"""

from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        possible = False
        if Counter(s1) == Counter(s2):
            count = 0
            for i, j in zip(s1, s2):
                if i != j:
                    count += 1

            if count <= 2:
                possible = True

        return possible


def main():
    s1 = "abcd"
    s2 = "dcba"
    result = Solution().areAlmostEqual(s1, s2)
    print(result)


if __name__ == '__main__':
    main()
