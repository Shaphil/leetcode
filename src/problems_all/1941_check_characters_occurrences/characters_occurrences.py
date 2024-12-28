"""
Runtime:            0 ms
Beats:              100.00%
Memory:             17.95 MB
Beats:              7.93%
Submission:         https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/submissions/1490756353/
Time complexity:    O(n)
Space complexity:   O(n)
Topics:             #hash-table, #string, #counting
Solved By:          #hash-set, #counting
"""

from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        values_count = set(counter.values())
        return True if len(values_count) == 1 else False


if __name__ == '__main__':
    s = "aaabb"
    result = Solution().areOccurrencesEqual(s)
    print(result)
