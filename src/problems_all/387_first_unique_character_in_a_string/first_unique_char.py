"""
Runtime:            26 ms
Beats:              97.86%
Memory:             18.11 MB
Beats:              37.03%
Time complexity:    O(n)
Space complexity:   O(1)
Topics:             #hash-table, #string, #queue, #counting
Solved By:          #hash-table
Submission:         https://leetcode.com/problems/first-unique-character-in-a-string/submissions/1692222676/
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for char in counter:
            if counter[char] == 1:
                return s.index(char)

        return -1


def main():
    s = "loveleetcode"
    result = Solution().firstUniqChar(s)
    print(result)


if __name__ == '__main__':
    main()
