"""
https://leetcode.com/problems/number-of-1-bits/description/

Runtime: 41 ms
Memory: 13.9 MB
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        bstr = bin(n)[2:]
        total = 0
        for i in bstr:
            if int(i) == 1:
                total += 1

        return total


def main():
    n = 123
    weight = Solution().hammingWeight(n)
    print(weight)


if __name__ == '__main__':
    main()
