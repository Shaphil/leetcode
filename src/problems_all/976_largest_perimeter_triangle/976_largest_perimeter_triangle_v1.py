"""
https://leetcode.com/problems/largest-perimeter-triangle/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/largest-perimeter-triangle/

Runtime: 206 ms
Memory: 15.4 MB
"""


from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        perimeter = 0
        desc = sorted(nums, reverse=True)
        for i in range(len(desc) - 2):
            a, b, c = desc[i: i + 3]

            tr1 = a + b > c
            tr2 = a + c > b
            tr3 = b + c > a
            if tr1 and tr2 and tr3:
                if a + b + c > perimeter:
                    perimeter = a + b + c
                    break

        return perimeter


def main():
    nums = [3, 6, 2, 3]
    perimeter = Solution().largestPerimeter(nums)
    print(perimeter)


if __name__ == '__main__':
    main()
