"""
Runtime:            31 ms
Beats:              67.65%
Memory:             50.39 MB
Beats:              21.78%
Submission:         https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/1508455372/
Time complexity:    O(n)
Space complexity:   O(h) avg, where `h` = tree height, O(n) worst
Topics:             #tree, #bfs, #dfs, #binary-tree
Solved By:          #dfs
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1]

            if triangle:
                last_row = triangle[-1]
                for j in range(len(last_row) - 1):
                    row.append(last_row[j] + last_row[j + 1])
                row.append(1)

            triangle.append(row)

        return triangle

if __name__ == '__main__':
    numRows = 5
    result = Solution().generate(numRows)
    print(result)
