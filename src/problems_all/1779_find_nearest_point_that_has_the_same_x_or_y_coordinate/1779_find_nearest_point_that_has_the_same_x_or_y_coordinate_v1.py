"""
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

Runtime: 699 ms
Memory: 19.3 MB
Submission - https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/submissions/866379885/
"""


from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        closest = float('inf')
        closest_idx = -1
        for i, point in enumerate(points):
            _x, _y = point
            if x == _x or y == _y:
                dist = abs(x - _x) + abs(y - _y)
                if dist < closest:
                    closest = dist
                    closest_idx = i

        return closest_idx


def main():
    x = 3
    y = 4
    points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
    closest = Solution().nearestValidPoint(x, y, points)
    print(closest)


if __name__ == '__main__':
    main()
