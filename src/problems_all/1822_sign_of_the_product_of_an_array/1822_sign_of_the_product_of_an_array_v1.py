"""
https://leetcode.com/problems/sign-of-the-product-of-an-array/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/sign-of-the-product-of-an-array/

Runtime: 64 ms
Memory: 14 MB
https://leetcode.com/problems/sign-of-the-product-of-an-array/submissions/866987116/
"""

from typing import List
from math import prod


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = prod(nums)
        return self.signFunc(product)

    def signFunc(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0


def main():
    nums = [9, 72, 34, 29, -49, -22, -77, -17, -66, -75, -44, -30, -24]
    result = Solution().arraySign(nums)
    print(result)


if __name__ == '__main__':
    main()
