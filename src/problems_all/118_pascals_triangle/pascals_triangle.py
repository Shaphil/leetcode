"""
Runtime:            0 ms
Beats:              100.00%
Memory:             19.28 MB
Beats:              70.13%
Submission:         https://leetcode.com/problems/pascals-triangle/submissions/2117452578/
Time complexity:    O(n^2)
Space complexity:   O(n^2)
Topics:             #array, #dynamic-programming
Solved By:          #array
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows + 1):
            row = [1]

            if triangle:
                last_row = triangle[-1]
                for j in range(len(last_row) - 1):
                    row.append(last_row[j] + last_row[j + 1])
                row.append(1)

            triangle.append(row)

        return triangle[numRows]

if __name__ == '__main__':
    numRows = 1
    result = Solution().generate(numRows)
    print(result)
