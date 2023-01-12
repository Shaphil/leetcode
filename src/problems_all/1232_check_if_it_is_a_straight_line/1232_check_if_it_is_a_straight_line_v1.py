"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/description/

Runtime: 52 ms
Memory: 14 MB
https://leetcode.com/problems/check-if-it-is-a-straight-line/submissions/336741338/
"""


from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if x2 - x1 == 0:
            slope = x1
        else:
            slope = (y2 - y1) / (x2 - x1)

        is_stright_line = True
        for i in range(1, len(coordinates) - 1):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i + 1]

            if x2 - x1 == 0:
                new_slope = x1
            else:
                new_slope = (y2 - y1) / (x2 - x1)

            if new_slope != slope:
                is_stright_line = False
                break

        return is_stright_line


def main():
    coordinates = [[-4, -3], [1, 0], [3, -1], [0, -1], [-5, 2]]
    result = Solution().checkStraightLine(coordinates)
    print(result)


if __name__ == '__main__':
    main()
