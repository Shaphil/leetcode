"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ('+', '-', '*', '/')
        op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }

        stack = []
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(op[i](b, a))

        return stack.pop()


def solve():
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    solution = Solution()
    print(solution.evalRPN(tokens))


if __name__ == '__main__':
    solve()
