"""
Runtime:    119 ms
Beats:      11.55%
Memory:     17.78 MB
Beats:      13.67%
Submission: https://leetcode.com/problems/optimal-partition-of-string/submissions/1465312049/
Topics:     #hash-table, #string, #greedy
Solved By:  #hash-table
"""

from collections import defaultdict


class Solution:
    def partitionString(self, s: str) -> int:
        freq = defaultdict(int)
        partitions = 0

        for char in s:
            freq[char] += 1
            if freq[char] > 1:
                partitions += 1
                freq = defaultdict(int)
                freq[char] = 1

        return partitions + 1


if __name__ == '__main__':
    s = "abacaba"
    result = Solution().partitionString(s)
    print(result)
