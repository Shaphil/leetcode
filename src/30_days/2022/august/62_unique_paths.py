"""
https://www.youtube.com/watch?v=IlEsdxuD4lY
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        last_row = [1] * n

        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + last_row[j]

            last_row = new_row

        return last_row[0]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
    print(s.uniquePaths(1, 1))
    print(s.uniquePaths(3, 2))
    print(s.uniquePaths(2, 10))
    print(s.uniquePaths(6, 7))
