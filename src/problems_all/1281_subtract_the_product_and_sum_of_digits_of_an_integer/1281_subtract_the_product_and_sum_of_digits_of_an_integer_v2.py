"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

Runtime: 34 ms
Memory: 13.9 MB
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total = 0
        product = 1

        while n > 0:
            i = n % 10
            total += i
            product *= i
            n //= 10

        result = product - total
        return result


def main():
    n = 4421
    result = Solution().subtractProductAndSum(n)
    print(result)


if __name__ == '__main__':
    main()
