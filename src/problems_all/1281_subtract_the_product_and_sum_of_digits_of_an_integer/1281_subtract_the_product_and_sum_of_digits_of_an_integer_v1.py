"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/?envType=study-plan&id=programming-skills-i
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

Runtime: 30 ms
Memory: 13.8 MB
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total = 0
        product = 1
        digits = map(int, list(str(n)))

        for i in digits:
            total += i
            product *= i

        result = product - total
        return result


def main():
    n = 4421
    result = Solution().subtractProductAndSum(n)
    print(result)


if __name__ == '__main__':
    main()
