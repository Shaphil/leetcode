"""
https://leetcode.com/problems/matrix-diagonal-sum/

Runtime: 102 ms
Memory: 14 MB
https://leetcode.com/problems/matrix-diagonal-sum/submissions/879165128/
"""


from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        _sum = 0
        _len = len(mat)
        mid = _len // 2

        for i in range(_len):
            # primary diagonal
            _sum += mat[i][i]

            # secondary diagonal
            _sum += mat[_len - 1 - i][i]

        if _len % 2 == 1:
            _sum -= mat[mid][mid]

        return _sum


def main():
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

    result = Solution().diagonalSum(mat)
    print(result)


if __name__ == '__main__':
    main()
