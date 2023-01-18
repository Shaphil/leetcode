"""
https://leetcode.com/problems/goal-parser-interpretation/


Runtime: 33 ms
Memory: 13.7 MB
"""


class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace('()', 'o')
        command = command.replace('(al)', 'al')
        return command


def main():
    command = "(al)G(al)()()G"
    result = Solution().interpret(command)
    print(result)


if __name__ == '__main__':
    main()
