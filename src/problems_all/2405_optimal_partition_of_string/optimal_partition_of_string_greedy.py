"""
Runtime:    51 ms
Beats:      52.86%
Memory:     17.50 MB
Beats:      20.40%
Submission: https://leetcode.com/problems/optimal-partition-of-string/submissions/1465325765/
Topics:     #hash-table, #string, #greedy
Solved By:  #greedy
"""


class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        partitions = 1

        for char in s:
            if char in seen:
                partitions += 1
                seen.clear()
            seen.add(char)

        return partitions


if __name__ == '__main__':
    s = "abacaba"
    result = Solution().partitionString(s)
    print(result)
