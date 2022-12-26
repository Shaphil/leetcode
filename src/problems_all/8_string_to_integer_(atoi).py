"""
https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        temp = num = ''
        hi = 2 ** 31 - 1
        lo = -2 ** 31
        prev_num = True
        signs = ['-', '+']

        s = s.strip()
        for c in s:
            if c in signs or c.isnumeric():
                temp += c
            elif prev_num and not c.isnumeric():
                break

        for c in temp:
            if c.isnumeric():
                num += c

        for c in temp:
            if c == '-':
                num = '-' + num
                break

        num = 0 if num == '' or num in signs else int(num)
        num = hi if num > hi else num
        num = lo if num < lo else num

        return num


def solve():
    s = "  +-+-+--1"
    solution = Solution()
    print(solution.myAtoi(s))


if __name__ == '__main__':
    solve()
