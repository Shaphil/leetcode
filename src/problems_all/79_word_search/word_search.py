"""
Runtime:            3231 ms
Beats:              81.79%
Memory:             17.51 MB
Beats:              5.64%
Submission:         https://leetcode.com/problems/word-search/submissions/1477947774/
Time complexity:    O(n^3)
Space complexity:   O(n^2)
Topics:             #backtracking, #bfs, #dfs
Solved By:          #dfs
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or board[row][col] != word[index]:
                return False

            visited[row][col] = True
            found = dfs(row - 1, col, index + 1) or dfs(row + 1, col, index + 1) or dfs(row, col - 1, index + 1) or dfs(
                row, col + 1, index + 1)
            visited[row][col] = False

            return found

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and dfs(row, col, 0):
                    return True

        return False


if __name__ == '__main__':
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word = "ABCCED"
    output = Solution().exist(board, word)
    print(output)
